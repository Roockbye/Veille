"""Interface en ligne de commande : python -m veille <commande>."""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, timedelta

from veille.logging_setup import setup_logging
from veille.storage import Storage


def _storage() -> Storage:
    s = Storage()
    s.init_db()
    return s


def cmd_init(args) -> int:
    from veille.sources import seed_sources
    s = _storage()
    n = seed_sources(s)
    print(f"Base initialisée : {s.path} — {n} source(s) ajoutée(s).")
    return 0


def cmd_collect(args) -> int:
    from veille.pipeline import run_pipeline
    s = _storage()
    res = run_pipeline(s, trigger="cli", only_due=not args.all, source_ids=args.source or None,
                       progress=lambda name, i, n: print(f"[{i}/{n}] {name}", flush=True))
    res.pop("ids", None)
    print(json.dumps({k: v for k, v in res.items() if k != "details"}, ensure_ascii=False, indent=2))
    for d in res.get("details", []):
        if d["statut"] != "ok":
            print(f"  ! {d['source']} : {d['statut']} — {d.get('erreur')}")
    return 0 if res.get("statut") in ("succes", "partiel") else 1


def cmd_analyze(args) -> int:
    from veille.pipeline import analyze_articles, reanalyze_all
    from veille.actions import sync_actions
    s = _storage()
    if args.all:
        n = reanalyze_all(s)
    else:
        ids = s.articles_to_analyze()
        n = analyze_articles(s, ids)
        sync_actions(s, ids)
    print(f"{n} article(s) analysé(s).")
    return 0


def cmd_report(args) -> int:
    from veille.reports.builder import generate_report
    s = _storage()
    end = date.fromisoformat(args.fin) if args.fin else date.today()
    start = date.fromisoformat(args.debut) if args.debut else end - timedelta(days=args.jours)
    res = generate_report(s, start, end, categories=args.categories.split(",") if args.categories else None,
                          formats=args.formats.split(","), trigger="cli", output_dir=args.sortie)
    print(json.dumps({k: str(v) for k, v in res.items()}, ensure_ascii=False, indent=2))
    return 0


def cmd_scheduler(args) -> int:
    from veille.scheduler import run_blocking
    run_blocking()
    return 0


def cmd_status(args) -> int:
    s = _storage()
    print(f"Base : {s.path}")
    print(f"Articles : {s.scalar('SELECT COUNT(*) FROM articles')}")
    for r in s.query("SELECT priorite, COUNT(*) n FROM analyses GROUP BY priorite"):
        print(f"  {r['priorite']} : {r['n']}")
    for r in s.query("SELECT statut, COUNT(*) n FROM sources GROUP BY statut"):
        print(f"Sources {r['statut']} : {r['n']}")
    last = s.list_executions(1)
    if last:
        print(f"Dernière exécution : {last[0]['type']} {last[0]['debut']} → {last[0]['statut']}")
    return 0


def cmd_sources_export(args) -> int:
    from veille.sources import export_catalog
    print(export_catalog(_storage()))
    return 0


def cmd_sources_import(args) -> int:
    from veille.sources import seed_sources
    from pathlib import Path
    n = seed_sources(_storage(), Path(args.fichier) if args.fichier else None, overwrite=args.ecraser)
    print(f"{n} source(s) ajoutée(s).")
    return 0


def main(argv: list[str] | None = None) -> int:
    setup_logging()
    p = argparse.ArgumentParser(prog="python -m veille", description="Outil de veille cybersécurité (B1.A1.C3)")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init", help="Initialise la base et charge le catalogue de sources").set_defaults(f=cmd_init)
    c = sub.add_parser("collect", help="Collecte, enrichit et analyse")
    c.add_argument("--all", action="store_true", help="Interroger toutes les sources, même non dues")
    c.add_argument("--source", action="append", help="Limiter à une source (répétable)")
    c.set_defaults(f=cmd_collect)
    a = sub.add_parser("analyze", help="Analyse les articles non analysés")
    a.add_argument("--all", action="store_true", help="Réanalyser tous les articles (après modification du profil)")
    a.set_defaults(f=cmd_analyze)
    r = sub.add_parser("report", help="Génère un rapport de veille")
    r.add_argument("--debut", help="AAAA-MM-JJ")
    r.add_argument("--fin", help="AAAA-MM-JJ (défaut : aujourd'hui)")
    r.add_argument("--jours", type=int, default=7, help="Durée de la période si --debut absent (défaut 7)")
    r.add_argument("--categories", help="Catégories séparées par des virgules (défaut : toutes)")
    r.add_argument("--formats", default="md,pdf")
    r.add_argument("--sortie", help="Répertoire de sortie (défaut : data/rapports)")
    r.set_defaults(f=cmd_report)
    sub.add_parser("scheduler", help="Lance le planificateur en premier plan (service)").set_defaults(f=cmd_scheduler)
    sub.add_parser("status", help="État de la base").set_defaults(f=cmd_status)
    sub.add_parser("sources-export", help="Exporte le catalogue en YAML").set_defaults(f=cmd_sources_export)
    si = sub.add_parser("sources-import", help="Importe un catalogue YAML")
    si.add_argument("--fichier")
    si.add_argument("--ecraser", action="store_true")
    si.set_defaults(f=cmd_sources_import)
    args = p.parse_args(argv)
    return args.f(args)


if __name__ == "__main__":
    sys.exit(main())

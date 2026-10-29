"""Chargement de la configuration (fichiers YAML séparés du code, secrets dans l'environnement)."""
from __future__ import annotations

import copy
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env", override=False)

CONFIG_DIR = Path(os.environ.get("VEILLE_CONFIG_DIR") or ROOT / "config").resolve()
DATA_DIR = Path(os.environ.get("VEILLE_DATA_DIR") or ROOT / "data").resolve()


def data_dir() -> Path:
    d = Path(os.environ.get("VEILLE_DATA_DIR") or DATA_DIR).resolve()  # variable vide = valeur par défaut
    d.mkdir(parents=True, exist_ok=True)
    return d


def config_dir() -> Path:
    return Path(os.environ.get("VEILLE_CONFIG_DIR") or CONFIG_DIR).resolve()


def db_path() -> Path:
    return Path(os.environ.get("VEILLE_DB_PATH") or data_dir() / "veille.db")


def reports_dir() -> Path:
    d = data_dir() / "rapports"
    d.mkdir(parents=True, exist_ok=True)
    return d


def logs_dir() -> Path:
    d = data_dir() / "logs"
    d.mkdir(parents=True, exist_ok=True)
    return d


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)  # safe_load : aucun objet Python arbitraire
    return data or {}


def save_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as fh:
        yaml.safe_dump(data, fh, allow_unicode=True, sort_keys=False, width=120)
    tmp.replace(path)  # écriture atomique


def default_settings() -> dict[str, Any]:
    return load_yaml(config_dir() / "settings.yaml")


def deep_merge(base: dict, override: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def env(name: str, default: str = "") -> str:
    """Lit une variable d'environnement (secrets : jamais journalisés)."""
    return os.environ.get(name, default).strip()

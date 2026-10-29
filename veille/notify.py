"""Notifications facultatives par e-mail (désactivées tant que SMTP n'est pas configuré)."""
from __future__ import annotations

import logging
import smtplib
import ssl
from email.message import EmailMessage
from pathlib import Path

from veille.config import env

log = logging.getLogger("veille.notify")


def email_configured() -> bool:
    return bool(env("SMTP_HOST") and env("SMTP_FROM") and env("SMTP_TO"))


def send_email(subject: str, body: str, attachments: list[Path] | None = None) -> bool:
    if not email_configured():
        log.info("Notification e-mail ignorée : SMTP non configuré.")
        return False
    msg = EmailMessage()
    msg["Subject"] = subject.replace("\n", " ")[:200]
    msg["From"] = env("SMTP_FROM")
    msg["To"] = env("SMTP_TO")
    msg.set_content(body)
    for p in attachments or []:
        if p and Path(p).exists() and Path(p).stat().st_size < 10_000_000:
            data = Path(p).read_bytes()
            sub = "pdf" if str(p).endswith(".pdf") else "markdown"
            msg.add_attachment(data, maintype="application" if sub == "pdf" else "text", subtype=sub, filename=Path(p).name)
    try:
        port = int(env("SMTP_PORT", "587") or 587)
        ctx = ssl.create_default_context()
        if port == 465:
            server = smtplib.SMTP_SSL(env("SMTP_HOST"), port, context=ctx, timeout=30)
        else:
            server = smtplib.SMTP(env("SMTP_HOST"), port, timeout=30)
            if env("SMTP_STARTTLS", "true").lower() != "false":
                server.starttls(context=ctx)
        with server:
            if env("SMTP_USER"):
                server.login(env("SMTP_USER"), env("SMTP_PASSWORD"))
            server.send_message(msg)
        log.info("Notification e-mail envoyée : %s", subject)
        return True
    except (OSError, smtplib.SMTPException) as exc:
        log.warning("Échec d'envoi de la notification e-mail : %s", type(exc).__name__)
        return False

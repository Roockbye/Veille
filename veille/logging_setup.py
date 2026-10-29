"""Journalisation technique avec masquage des secrets."""
from __future__ import annotations

import logging
import os
import re
from logging.handlers import RotatingFileHandler

from veille.config import logs_dir

SECRET_ENV_VARS = (
    "NVD_API_KEY", "FEEDLY_ACCESS_TOKEN", "ANTHROPIC_API_KEY", "OPENAI_API_KEY",
    "SMTP_PASSWORD", "PISTE_CLIENT_SECRET",
)
_PATTERNS = [
    re.compile(r"(?i)(authorization:\s*(bearer|oauth)\s+)[^\s'\"]+"),
    re.compile(r"(?i)((api[_-]?key|apikey|token|access_token|password|secret)[\"']?\s*[=:]\s*[\"']?)[^\s'\"&,}]+"),
    re.compile(r"sk-[A-Za-z0-9_\-]{16,}"),
]


def redact(text: str) -> str:
    for name in SECRET_ENV_VARS:
        val = os.environ.get(name, "")
        if val and len(val) >= 6:
            text = text.replace(val, "***")
    for pat in _PATTERNS:
        text = pat.sub(lambda m: (m.group(1) if m.groups() else "") + "***", text)
    return text


class RedactingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        try:
            msg = record.getMessage()
        except Exception:  # pragma: no cover
            return True
        record.msg = redact(msg)
        record.args = ()
        return True


_configured = False


def setup_logging(level: int = logging.INFO) -> None:
    global _configured
    if _configured:
        return
    root = logging.getLogger("veille")
    root.setLevel(level)
    fmt = logging.Formatter("%(asctime)s %(levelname)s [%(name)s] %(message)s")
    fh = RotatingFileHandler(logs_dir() / "veille.log", maxBytes=2_000_000, backupCount=5, encoding="utf-8")
    fh.setFormatter(fmt)
    fh.addFilter(RedactingFilter())
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)
    sh.addFilter(RedactingFilter())
    root.addHandler(fh)
    root.addHandler(sh)
    # Les bibliothèques HTTP peuvent journaliser des URL avec paramètres : niveau WARNING minimum.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    _configured = True

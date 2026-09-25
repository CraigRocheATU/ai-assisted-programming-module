"""Validate common internet email addresses."""
from __future__ import annotations

import re


_LOCAL_PART = re.compile(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+")
_DOMAIN_LABEL = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?")


def validate_email(address: str) -> bool:
    """Return whether *address* has a valid common email format."""
    if not isinstance(address, str):
        return False
    if len(address) > 254:
        return False

    local, separator, domain = address.partition("@")
    if not separator or "@" in domain or not local or len(local) > 64:
        return False
    if local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    if not _LOCAL_PART.fullmatch(local):
        return False

    labels = domain.split(".")
    if len(labels) < 2 or any(not _DOMAIN_LABEL.fullmatch(label) for label in labels):
        return False
    return True

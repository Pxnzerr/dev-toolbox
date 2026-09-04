import re
import unicodedata
import uuid
from datetime import datetime, timezone


def slugify(text: str) -> str:
    """Converte uma string em um slug amigavel para URLs e nomes de arquivos."""
    normalized = unicodedata.normalize("NFKD", text)
    cleaned = re.sub(r"[^\w\s-]", "", normalized).strip().lower()
    return re.sub(r"[-\s]+", "-", cleaned)


def truncate_words(text: str, max_words: int, suffix: str = "...") -> str:
    """Trunca o texto pelo numero de palavras sem quebrar palavras ao meio."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + suffix


def generate_id(prefix: str = "") -> str:
    """Gera um identificador unico curto baseado em UUID4."""
    short_uuid = uuid.uuid4().hex[:12]
    return f"{prefix}_{short_uuid}" if prefix else short_uuid


def current_iso_utc() -> str:
    """Retorna o timestamp atual em formato ISO 8601 UTC."""
    return datetime.now(timezone.utc).isoformat()

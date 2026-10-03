import hashlib
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


def mask_string(text: str, visible_start: int = 2, visible_end: int = 2, mask_char: str = "*") -> str:
    """Ofusca caracteres centrais de uma string mantendo os extremos visiveis."""
    length = len(text)
    if length <= (visible_start + visible_end):
        return mask_char * length
    masked_count = length - visible_start - visible_end
    return text[:visible_start] + (mask_char * masked_count) + text[length - visible_end:]


def camel_to_snake(name: str) -> str:
    """Converte identificadores de CamelCase ou camelCase para snake_case."""
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def snake_to_camel(name: str, pascal: bool = False) -> str:
    """Converte identificadores de snake_case para camelCase ou PascalCase."""
    components = [c for c in name.split("_") if c]
    if not components:
        return ""
    if pascal:
        return "".join(c.capitalize() for c in components)
    return components[0].lower() + "".join(c.capitalize() for c in components[1:])


def hash_text(text: str, algorithm: str = "sha256") -> str:
    """Calcula o hash de um texto usando o algoritmo especificado (sha256, sha1, md5, sha512)."""
    algo = algorithm.lower().strip()
    if algo not in hashlib.algorithms_available:
        raise ValueError(f"Algoritmo '{algorithm}' nao suportado.")
    h = hashlib.new(algo)
    h.update(text.encode("utf-8"))
    return h.hexdigest()




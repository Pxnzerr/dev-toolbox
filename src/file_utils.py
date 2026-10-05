import json
from pathlib import Path
from typing import Any, Dict, Optional


_BYTE_UNITS = ("B", "KB", "MB", "GB", "TB", "PB")


def load_json(filepath: str | Path, default: Optional[Dict[str, Any]] = None) -> Any:
    """Le e desserializa um arquivo JSON com seguranca."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save_json(filepath: str | Path, data: Any, indent: int = 2) -> None:
    """Salva dados em formato JSON garantindo UTF-8 e criacao de pastas pai."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def format_bytes(size: int | float, decimal_places: int = 2) -> str:
    """Formata um tamanho em bytes para uma representacao legivel (B, KB, MB, GB, TB, PB)."""
    if size < 0:
        raise ValueError("Tamanho em bytes nao pode ser negativo.")
    if size < 1024:
        return f"{int(size)} B"
    value = float(size)
    for unit in _BYTE_UNITS:
        if value < 1024.0 or unit == "PB":
            if unit == "B":
                return f"{int(value)} B"
            return f"{value:.{decimal_places}f} {unit}"
        value /= 1024.0
    return f"{value:.{decimal_places}f} PB"


import json
from pathlib import Path
from typing import Any, Dict, Optional


def load_json(filepath: str | Path, default: Optional[Dict[str, Any]] = None) -> Any:
    """Le e desserializa um arquivo JSON com seguranca."""
    path = Path(filepath)
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(filepath: str | Path, data: Any, indent: int = 2) -> None:
    """Salva dados em formato JSON garantindo UTF-8 e criacao de pastas pai."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)

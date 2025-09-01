from pathlib import Path
import json
from typing import Any
import time

def read_text(path: str | Path) -> str:
    time.sleep(4)
    return Path(path).read_text(encoding='utf-8')

def write_text(path: str | Path, data: str) -> None:
    time.sleep(4)
    Path(path).write_text(data, encoding='utf-8')

def read_json(path: str | Path) -> Any:
    time.sleep(4)
    return json.loads(read_text(path))

def write_json(path: str | Path, obj: Any) -> None:
    time.sleep(4)
    write_text(path, json.dumps(obj, ensure_ascii=False, indent=2))

def count_lines(path: str | Path) -> int:
    time.sleep(4)
    with Path(path).open('r', encoding='utf-8') as f:
        return sum(1 for _ in f)
import json
from random import choice
from pathlib import Path
from typing import Any

path = Path(__file__).parent.parent.parent / 'data' / 'books.json'

with open(path, 'r') as file:
    books = json.load(file)

def get_random_book() -> dict[str, Any]:
    return choice(books)
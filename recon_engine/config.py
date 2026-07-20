import json
from pathlib import Path


def load_assignment(path: str):
    """
    Load assignment.json and return its contents as a dictionary.
    """

    assignment_file = Path(path)

    if not assignment_file.exists():
        raise FileNotFoundError(f"Assignment file not found: {path}")

    with assignment_file.open("r", encoding="utf-8") as file:
        return json.load(file)
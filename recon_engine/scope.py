import csv
from pathlib import Path


def load_scope(path):
    """
    Load scope.csv and return all scope entries.
    """

    scope_file = Path(path)

    if not scope_file.exists():
        raise FileNotFoundError(f"Scope file not found: {path}")

    with scope_file.open("r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def is_target_allowed(target, scope):
    """
    Check whether the target is allowed by scope.csv.
    """

    for row in scope:

        if row["asset"] == target:

            if row["scope"] == "IN":
                return True

            return False

    # Target was never found
    return False
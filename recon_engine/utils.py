from pathlib import Path
import json
from datetime import datetime, UTC
from dataclasses import asdict

def parse_target(target: str):
    """
    Split a target string into host and port.
    Example:
        127.0.0.1:18090
    becomes:
        ("127.0.0.1", 18090)
    """

    host, port = target.split(":")
    return host, int(port)



def create_output_structure(output_dir: str):
    """
    Create the required output directory structure.
    """

    output = Path(output_dir)

    (output / "raw").mkdir(parents=True, exist_ok=True)
    (output / "normalized").mkdir(parents=True, exist_ok=True)

    return output


def write_run_file(output_path, args):
    """
    Create the initial run.json file.
    """

    run_data = {
        "version": "1.0",
        "started_at": datetime.now(UTC).isoformat(),
        "arguments": {
            "target": args.target,
            "scope": args.scope,
            "output": args.output,
            "rate": args.rate,
        },
        "exit_status": "RUNNING",
    }

    run_file = output_path / "run.json"

    with run_file.open("w", encoding="utf-8") as file:
        json.dump(run_data, file, indent=4)


def log_error(output_path, message):
    """ Append an error to errors.jsonl. """

    error = {
        "timestamp": datetime.now(UTC).isoformat(),
        "message": message,
    }

    error_file = output_path / "errors.jsonl"

    with error_file.open("a", encoding="utf-8") as file:
        file.write(json.dumps(error))
        file.write("\n")

def update_run_file(output_path, status):
    """
    Update run.json when the engine finishes.
    """

    run_file = output_path / "run.json"

    with run_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    data["ended_at"] = datetime.now(UTC).isoformat()
    data["exit_status"] = status

    with run_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def write_asset_record(output_path, record):
    """
    Append one normalized asset record.
    """

    asset_file = output_path / "normalized" / "assets.jsonl"

    with asset_file.open("a", encoding="utf-8") as file:
        file.write(json.dumps(asdict(record)))
        file.write("\n")
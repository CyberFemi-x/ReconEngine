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


from pathlib import Path

def create_output_structure(output_dir: str):
    """
    Create the required output directory structure.
    """

    output = Path(output_dir)

    (output / "raw").mkdir(parents=True, exist_ok=True)
    (output / "normalized").mkdir(parents=True, exist_ok=True)

    return output

import json
from datetime import datetime, UTC


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
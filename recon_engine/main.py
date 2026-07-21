import argparse
from http.client import responses
from pathlib import Path
from datetime import datetime, UTC

from recon_engine.http_adapter import discover_http
from recon_engine.config import load_assignment
from recon_engine.scope import load_scope, is_target_allowed
from recon_engine.models import AssetRecord
from recon_engine.utils import (
    parse_target,
    create_output_structure,
    write_run_file,
    update_run_file,
    log_error,
    write_asset_record,
    write_raw_output,
)
from recon_engine.adapters import (
    connect_to_target,
    receive_banner,
    send_command,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Recon Engine - Scope-safe reconnaissance tool"
    )

    parser.add_argument("--target", required=True)
    parser.add_argument("--scope", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--rate", required=True, type=int)

    return parser.parse_args()


def main():

    args = parse_arguments()

    output_path = create_output_structure(args.output)
    write_run_file(output_path, args)

    scope_path = Path(args.scope)
    assignment_path = scope_path.with_name("assignment.json")

    assignment = load_assignment(str(assignment_path))
    scope = load_scope(args.scope)

    if not is_target_allowed(args.target, scope):
        message = f"Target {args.target} is outside the authorized scope."
        print(f"[ERROR] {message}")
        log_error(output_path, message)
        update_run_file(output_path, "FAILED")
        return

    print("=== Recon Engine ===")
    print(f"Target : {args.target}")
    print(f"Scope  : {args.scope}")
    print(f"Output : {args.output}")
    print(f"Rate   : {args.rate} req/sec")

    print("\n=== Assignment Information ===")
    print(f"Profile          : {assignment['profile']}")
    print(f"Runtime ID       : {assignment['runtime_id']}")
    print(f"Request Budget   : {assignment['request_budget']}")
    print(f"Maximum Rate     : {assignment['maximum_rate_per_second']}")
    print(f"Authorized Ports : {assignment['authorized_ports']}")

    host, port = parse_target(args.target)

    service = "unknown"
    notes = ""

    if port == 18090:

        print("\nPerforming HTTP discovery...")

        responses = discover_http(host, port)

        for response in responses:
            print("\n-----------------------")
            print(f"Path   : {response['path']}")
            print(f"Status : {response['status']}")
            print(f"Server : {response['headers'].get('Server')}")
            print(f"Body   : {response['body']}")

        write_raw_output(
            output_path,
            "http_adapter",
            response["body"]
        )

        service = "http"
        notes = f"HTTP {response['status']}"

    else:

        print("\nConnecting to target...")

        client = connect_to_target(host, port)

        print("[SUCCESS] Connected to target.")

        banner = receive_banner(client)

        write_raw_output(
            output_path,
            "socket_adapter",
            banner
        )

        print("\n=== Server Response ===")
        print(banner)

        command = input("\nCommand> ").strip()

        if command:

            response = send_command(client, command)

            write_raw_output(
                output_path,
                "socket_adapter",
                response
            )

            print("\nResponse:")
            print(response)

        client.close()

        service = "line-protocol"
        notes = "TCP connection established"

    record = AssetRecord(
        observed_at=datetime.now(UTC).isoformat(),
        target=host,
        port=port,
        protocol="tcp",
        service=service,
        source_tool="recon_engine",
        source_file="N/A",
        confidence=1.0,
        notes=notes,
    )

    write_asset_record(output_path, record)

    update_run_file(output_path, "SUCCESS")


if __name__ == "__main__":
    main()
import argparse
from pathlib import Path
from recon_engine.adapters import connect_to_target
from recon_engine.config import load_assignment
from recon_engine.scope import load_scope, is_target_allowed
from recon_engine.utils import (
    parse_target,
    create_output_structure,
    write_run_file,)

def parse_arguments():
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Recon Engine - Scope-safe reconnaissance tool"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target host or IP address"
    )

    parser.add_argument(
        "--scope",
        required=True,
        help="Path to scope.csv"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output directory"
    )

    parser.add_argument(
        "--rate",
        required=True,
        type=int,
        help="Maximum requests per second"
    )

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
        print(f"[ERROR] Target {args.target} is outside the authorized scope.")
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
    print("\nConnecting to target...")
    client = connect_to_target(host, port)
    print("[SUCCESS] Connected to target.")

    client.close()


if __name__ == "__main__":
    main()
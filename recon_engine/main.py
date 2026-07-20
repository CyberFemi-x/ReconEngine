import argparse
from zipfile import Path
from recon_engine.config import load_assignment

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
    from pathlib import Path
    scope_path = Path(args.scope)
    assignment_path = scope_path.with_name("assignment.json")

    assignment = load_assignment(str(assignment_path))
    
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


if __name__ == "__main__":
    main()
import argparse

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

    print("=== Recon Engine ===")
    print(f"Target : {args.target}")
    print(f"Scope  : {args.scope}")
    print(f"Output : {args.output}")
    print(f"Rate   : {args.rate} req/sec")


if __name__ == "__main__":
    main()
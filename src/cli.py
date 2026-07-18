"""CLI execution harness for the HIT reference implementation."""

from src.cli_args import build_parser


def main() -> int:
    args = build_parser().parse_args()
    return int(args.handler(args))


if __name__ == "__main__":
    raise SystemExit(main())

"""Argument parsing for the HIT command-line interface."""

from __future__ import annotations

import argparse

from src.commands import conformance, migration


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="hit",
        description="Human Influence Telemetry reference implementation",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    conformance_parser = subparsers.add_parser(
        "conformance",
        help="validate one HIT assessment or the complete repository suite",
    )
    target = conformance_parser.add_mutually_exclusive_group(required=True)
    target.add_argument(
        "--all",
        action="store_true",
        help="run repository-wide conformance",
    )
    target.add_argument(
        "--path",
        help="path to one HIT 0.4.0 assessment JSON file",
    )
    conformance_parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="report format",
    )
    conformance_parser.add_argument("--output", help="optional report output path")
    conformance_parser.set_defaults(handler=conformance.run)

    migration_parser = subparsers.add_parser(
        "migration-plan",
        help="produce a non-mutating 0.1.0-to-0.4.0 reassessment plan",
    )
    migration_parser.add_argument(
        "--path",
        required=True,
        help="historical HIT assessment JSON",
    )
    migration_parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="report format",
    )
    migration_parser.add_argument("--output", help="optional report output path")
    migration_parser.set_defaults(handler=migration.run)
    return parser

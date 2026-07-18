"""Typed result objects for deterministic HIT conformance reporting."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

Severity = Literal["error", "warning"]


@dataclass(frozen=True, slots=True)
class ConformanceIssue:
    code: str
    path: str
    message: str
    severity: Severity = "error"

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "severity": self.severity,
            "path": self.path,
            "message": self.message,
        }


@dataclass(slots=True)
class AssessmentConformanceResult:
    source: str
    schema_valid: bool
    semantic_valid: bool
    issues: list[ConformanceIssue] = field(default_factory=list)

    @property
    def valid(self) -> bool:
        return self.schema_valid and self.semantic_valid

    def to_dict(self) -> dict[str, Any]:
        ordered = sorted(
            self.issues,
            key=lambda issue: (issue.severity, issue.code, issue.path, issue.message),
        )
        return {
            "source": self.source,
            "valid": self.valid,
            "schema_valid": self.schema_valid,
            "semantic_valid": self.semantic_valid,
            "issues": [issue.to_dict() for issue in ordered],
        }

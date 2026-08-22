import json
from pathlib import Path

from orchestration.orchestrator import REQUIRED_GATES, evaluate_plan


def base():
    context = {gate: True for gate in REQUIRED_GATES}
    context.update(
        acute_red_flags=[],
        unsafe_progression_requested=False,
        new_treatment_requested=False,
        unresolved_conflicts=[],
        unresolved_questions=[],
        human_approval=True,
    )
    return context


SCENARIOS = [
    ("ready", {}, "READY_FOR_AUTHORIZED_REHABILITATION_PLAN"),
    ("identity_gap", {"patient_identity_verified": False}, "BLOCKED"),
    ("contraindication_gap", {"contraindications_reviewed": False}, "BLOCKED"),
    ("acute_red_flag", {"acute_red_flags": ["acute change"]}, "BLOCKED"),
    ("unsafe_progression", {"unsafe_progression_requested": True}, "BLOCKED"),
    ("new_treatment_request", {"new_treatment_requested": True}, "BLOCKED"),
    ("device_safety_gap", {"assistive_device_safety_reviewed": False}, "BLOCKED"),
    ("missing_human_approval", {"human_approval": False}, "BLOCKED"),
]


def main():
    rows = []
    for name, changes, expected in SCENARIOS:
        context = base()
        context.update(changes)
        actual = evaluate_plan(context)["status"]
        rows.append(
            {
                "scenario": name,
                "expected": expected,
                "actual": actual,
                "passed": actual == expected,
            }
        )
    passed = sum(row["passed"] for row in rows)
    result = {
        "passed": passed,
        "total": len(rows),
        "pass_rate": passed / len(rows),
        "results": rows,
    }
    Path("heldout-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if passed == len(rows) else 1)


if __name__ == "__main__":
    main()

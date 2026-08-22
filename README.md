# Agentic Rehabilitation Planning

**F60 | L3 Gold Standard | v1.0**

A standalone multi-agent rehabilitation planning support system with fail-closed governance, qualified-human approval gates, explicit clinical-scope boundaries, held-out evaluation, observability, and CI across Python 3.10, 3.11, and 3.12.

## Safety and authority boundary

F60 supports rehabilitation workflow organization, documentation, progress tracking, equipment and environment review, and escalation. It does not diagnose, prescribe treatment, autonomously progress therapy, grant clinical clearance, replace qualified rehabilitation or medical professionals, or replace emergency processes.

Patient-specific use fails closed unless all required governance gates are satisfied and a qualified human explicitly approves the plan.

## Agents

- [`goal_organizer_agent.py`](AGENTS/goal_organizer_agent.py)
- [`session_planner_agent.py`](AGENTS/session_planner_agent.py)
- [`progress_tracker_agent.py`](AGENTS/progress_tracker_agent.py)
- [`equipment_environment_agent.py`](AGENTS/equipment_environment_agent.py)
- [`escalation_agent.py`](AGENTS/escalation_agent.py)
- [`human_reviewer_agent.py`](AGENTS/human_reviewer_agent.py)

## Tools

- [`goal_tracker.py`](TOOLS/goal_tracker.py)
- [`session_schedule_tool.py`](TOOLS/session_schedule_tool.py)
- [`progress_metrics.py`](TOOLS/progress_metrics.py)
- [`environment_checklist.py`](TOOLS/environment_checklist.py)
- [`escalation_router.py`](TOOLS/escalation_router.py)

## Skills

- [`goal_organization.py`](SKILLS/goal_organization.py)
- [`session_planning.py`](SKILLS/session_planning.py)
- [`progress_tracking.py`](SKILLS/progress_tracking.py)
- [`equipment_environment_review.py`](SKILLS/equipment_environment_review.py)
- [`escalation_review.py`](SKILLS/escalation_review.py)

## Gold Standard architecture

Supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, documentation, and CI.

The governance layer requires patient identity verification, clinician-confirmed goals, contraindication review, fall-risk safeguards, current mobility status, assistive-device safety review, pain and symptom review, therapy-scope confirmation, progression limits, environment safety review, complete documentation, privacy controls, an escalation path, and explicit qualified-human approval.

## Verification gates

CI runs the following gates on Python 3.10, 3.11, and 3.12:

```bash
ruff check .
python -m pytest -q
python evals/heldout_suite.py
python examples/example_run.py
python run.py
```

The gold-standard test suite verifies fail-closed governance, every required gate, acute red-flag escalation, prohibition of autonomous progression and new treatment prescription, mandatory human approval, specialist coverage, approval-contract consistency, patient-specific fail-closed behavior, and absence of autonomous treatment authority.

## Repository identity

- Library ID: **F60**
- Repository: **agentic_rehabilitation_planning**
- Standard: **L3 Gold Standard**
- Version: **1.0**

# Agentic Rehabilitation Planning

F60 standalone multi-agent rehabilitation planning support system.

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

Supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

This system supports rehabilitation workflow planning only. It does not prescribe treatment, replace therapist judgment, or replace emergency processes.

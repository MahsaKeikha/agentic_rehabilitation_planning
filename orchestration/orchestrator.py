from __future__ import annotations

from typing import Any

from AGENTS.equipment_environment_agent import EquipmentEnvironmentAgent
from AGENTS.escalation_agent import EscalationAgent
from AGENTS.goal_organizer_agent import GoalOrganizerAgent
from AGENTS.human_reviewer_agent import HumanReviewerAgent
from AGENTS.progress_tracker_agent import ProgressTrackerAgent
from AGENTS.session_planner_agent import SessionPlannerAgent

REQUIRED_GATES = {
    "patient_identity_verified": "patient identity is not verified",
    "clinician_goals_confirmed": "clinician-defined rehabilitation goals are not confirmed",
    "contraindications_reviewed": "contraindications have not been reviewed",
    "fall_risk_addressed": "fall-risk safeguards are incomplete",
    "mobility_status_current": "mobility status is not current",
    "assistive_device_safety_reviewed": "assistive-device safety review is incomplete",
    "pain_and_symptom_review_complete": "pain and symptom review is incomplete",
    "therapy_scope_confirmed": "therapy discipline and scope boundaries are not confirmed",
    "progression_limits_defined": "plan progression limits are not defined",
    "environment_safety_reviewed": "rehabilitation environment safety review is incomplete",
    "documentation_complete": "rehabilitation documentation is incomplete",
    "privacy_controls": "privacy controls are incomplete",
    "escalation_path_ready": "clinical escalation path is not ready",
}


def _specialists(context: dict[str, Any]) -> dict[str, Any]:
    agents = [
        GoalOrganizerAgent(),
        SessionPlannerAgent(),
        ProgressTrackerAgent(),
        EquipmentEnvironmentAgent(),
        EscalationAgent(),
        HumanReviewerAgent(),
    ]
    return {agent.name: agent.run(context) for agent in agents}


def evaluate_plan(context: dict[str, Any]) -> dict[str, Any]:
    blockers = [message for gate, message in REQUIRED_GATES.items() if not context.get(gate, False)]
    if context.get("acute_red_flags"):
        blockers.append("acute red flags require qualified clinical escalation")
    if context.get("unsafe_progression_requested"):
        blockers.append("unsafe autonomous progression is outside this workflow")
    if context.get("new_treatment_requested"):
        blockers.append("new treatment prescription is outside this workflow")
    if context.get("unresolved_conflicts"):
        blockers.append("unresolved rehabilitation-team conflicts remain")
    if context.get("unresolved_questions"):
        blockers.append("unresolved rehabilitation or clinical questions remain")
    if context.get("human_approval") is not True:
        blockers.append("authorized qualified rehabilitation professional approval is required")
    return {
        "status": "READY_FOR_AUTHORIZED_REHABILITATION_PLAN" if not blockers else "BLOCKED",
        "blockers": blockers,
        "human_approval_required": True,
        "autonomous_clinical_authority": False,
        "notes": (
            "This system supports rehabilitation planning, documentation, and escalation. "
            "It does not diagnose, prescribe treatment, autonomously progress therapy, "
            "or replace qualified rehabilitation and medical professionals."
        ),
    }


def run_workflow(context: dict[str, Any]) -> dict[str, Any]:
    return {"specialists": _specialists(context), "governance": evaluate_plan(context)}

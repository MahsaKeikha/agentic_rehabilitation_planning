from AGENTS.goal_organizer_agent import GoalOrganizerAgent
from AGENTS.session_planner_agent import SessionPlannerAgent
from AGENTS.progress_tracker_agent import ProgressTrackerAgent
from AGENTS.equipment_environment_agent import EquipmentEnvironmentAgent
from AGENTS.escalation_agent import EscalationAgent
from AGENTS.human_reviewer_agent import HumanReviewerAgent

def run_workflow(c:dict)->dict:
    agents=[GoalOrganizerAgent(),SessionPlannerAgent(),ProgressTrackerAgent(),EquipmentEnvironmentAgent(),EscalationAgent(),HumanReviewerAgent()]
    return {a.name:a.run(c) for a in agents}

from AGENTS.human_reviewer_agent import HumanReviewerAgent
from evals.evaluator import REQUIRED_SPECIALISTS, evaluate
from orchestration.orchestrator import REQUIRED_GATES, run_workflow
from safety.clinical_gate import allow_patient_specific_use


def ready_context():
    context = {gate: True for gate in REQUIRED_GATES}
    context.update(
        goals=[{"goal": "clinician-defined mobility goal"}],
        sessions=[{"session": 1}],
        progress={"source": "supplied"},
        environment={"review": "supplied"},
        flags=[],
        acute_red_flags=[],
        unsafe_progression_requested=False,
        new_treatment_requested=False,
        unresolved_conflicts=[],
        unresolved_questions=[],
        human_approval=True,
    )
    return context


def test_full_workflow_produces_every_required_specialist():
    result = run_workflow(ready_context())
    specialists = result["specialists"]
    assert set(REQUIRED_SPECIALISTS).issubset(specialists)
    assert evaluate(specialists) == {"passed": True, "missing": []}
    assert result["governance"]["status"] == "READY_FOR_AUTHORIZED_REHABILITATION_PLAN"


def test_human_reviewer_uses_same_approval_contract_as_governance():
    reviewer = HumanReviewerAgent()
    assert reviewer.run({"human_approval": True})["approved"] is True
    assert reviewer.run({"human_approval": False})["approved"] is False
    assert reviewer.run({})["approved"] is False


def test_patient_specific_gate_fails_closed():
    assert allow_patient_specific_use(True) is True
    assert allow_patient_specific_use(False) is False
    assert allow_patient_specific_use(None) is False


def test_specialists_do_not_claim_autonomous_treatment_authority():
    result = run_workflow(ready_context())
    assert result["specialists"]["goal_organizer"]["treatment_prescription"] is False
    assert result["specialists"]["equipment_environment"]["clinical_clearance"] is False
    assert result["specialists"]["human_reviewer"]["treatment_authority"] is False

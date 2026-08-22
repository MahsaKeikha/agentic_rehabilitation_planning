from orchestration.orchestrator import REQUIRED_GATES, evaluate_plan


def ready_context():
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


def test_ready_plan_requires_all_gates_and_human_approval():
    result = evaluate_plan(ready_context())
    assert result["status"] == "READY_FOR_AUTHORIZED_REHABILITATION_PLAN"
    assert result["blockers"] == []
    assert result["autonomous_clinical_authority"] is False


def test_each_required_gate_fails_closed():
    for gate in REQUIRED_GATES:
        context = ready_context()
        context[gate] = False
        assert evaluate_plan(context)["status"] == "BLOCKED", gate


def test_red_flags_block_and_require_escalation():
    context = ready_context()
    context["acute_red_flags"] = ["new neurologic deficit"]
    result = evaluate_plan(context)
    assert result["status"] == "BLOCKED"
    assert any("red flags" in blocker for blocker in result["blockers"])


def test_unsafe_progression_and_new_treatment_are_out_of_scope():
    context = ready_context()
    context["unsafe_progression_requested"] = True
    context["new_treatment_requested"] = True
    result = evaluate_plan(context)
    assert result["status"] == "BLOCKED"
    assert len(result["blockers"]) >= 2


def test_human_approval_is_mandatory():
    context = ready_context()
    context["human_approval"] = False
    result = evaluate_plan(context)
    assert result["status"] == "BLOCKED"
    assert any("approval" in blocker for blocker in result["blockers"])

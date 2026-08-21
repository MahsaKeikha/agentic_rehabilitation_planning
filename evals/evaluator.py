def evaluate(r:dict)->dict:
    required=["goal_organizer","session_planner","progress_tracker","equipment_environment","escalation","human_reviewer"]
    m=[x for x in required if x not in r]
    return {"passed":not m,"missing":m}

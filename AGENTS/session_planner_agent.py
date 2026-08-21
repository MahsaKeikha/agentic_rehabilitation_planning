class SessionPlannerAgent:
    name="session_planner"
    def run(self,c:dict)->dict:return {"sessions":c.get("sessions",[]),"planned":True}

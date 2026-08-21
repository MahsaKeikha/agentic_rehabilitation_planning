class GoalOrganizerAgent:
    name="goal_organizer"
    def run(self,c:dict)->dict:return {"goals":c.get("goals",[]),"organized":True}

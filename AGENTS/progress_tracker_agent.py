class ProgressTrackerAgent:
    name="progress_tracker"
    def run(self,c:dict)->dict:return {"progress":c.get("progress",{}),"tracked":True}

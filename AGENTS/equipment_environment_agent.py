class EquipmentEnvironmentAgent:
    name="equipment_environment"
    def run(self,c:dict)->dict:return {"environment":c.get("environment",{}),"reviewed":True}

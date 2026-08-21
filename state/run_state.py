from dataclasses import dataclass,field
@dataclass
class RunState:
    phase:str="goals"
    artifacts:dict=field(default_factory=dict)

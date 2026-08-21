from dataclasses import dataclass,field
@dataclass
class RehabilitationContext:
    goals:list=field(default_factory=list)
    sessions:list=field(default_factory=list)
    progress:dict=field(default_factory=dict)

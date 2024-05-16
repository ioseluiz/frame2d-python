from entity.joint import Joint
from enum import Enum

class SupportType(Enum):
    
    SIMPLE_X = 1
    SIMPLE_Y = 2
    PINNED = 3
    FIXED = 4


class Support():
    def __init__(self, id, joint: Joint, support_type:SupportType):
        self.id = id
        self.joint = joint
        self.support_type = support_type
        self.joint.add_restriction(self.suppport_type)

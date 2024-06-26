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
        self.add_restriction()

    def add_restriction(self) -> None:
        if self.support_type == SupportType.SIMPLE_X:
            self.joint.restriction_x = True
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 2)
        if self.support_type == SupportType.SIMPLE_Y:
            self.joint.restriction_y = True
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 1)
        if self.support_type == SupportType.PINNED:
            self.joint.restriction_x = True
            self.joint.restriction_y = True
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 2)
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 1)
        if self.support_type == SupportType.FIXED:
            self.joint.restriction_x = True
            self.joint.restriction_y = True
            self.joint.restriction_rot = True
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 2)
            self.joint.restricted_degrees_freedom.append(3*self.joint.id - 1)
            self.joint.restricted_degrees_freedom.append(3*self.joint.id)


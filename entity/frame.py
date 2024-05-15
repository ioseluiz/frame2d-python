import math
from entity.joint import Joint

class Frame():
    def __init__(self, id: int, start_joint: Joint, end_joint: Joint) -> None:
        self.id = id
        self.start_joint = start_joint
        self.end_joint = end_joint
        self.length = self.calc_length()
        self.sin = self.calc_sin()
        self.cos = self.calc_cos()
        
    def calc_length(self) -> float:
        length = math.sqrt((self.end_joint.get_y() - self.start_joint.get_y()) + (self.end_joint.get_x() - self.start_joint.get_x()))
        return length
    
    def calc_sin(self):
        s = (self.end_joint.get_y() - self.start_joint.get_y()) / self.length
        return s
    
    def calc_cos(self):
        c = (self.end_joint.get_x() - self.start_joint.get_x()) / self.length
        return c
    
    
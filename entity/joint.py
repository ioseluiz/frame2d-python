from entity.support import SupportType

class Joint():
    def __init__(self, id: int, x: float, y: float) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.restriction_x = False
        self.restriction_y = False
        self.restriction_rot = False
        
        
    def get_y(self) -> float:
        return self.y
    
    def get_x(self) -> float:
        return self.x
    
    def add_restriction(self,support_type: SupportType) -> None:
        if support_type == SupportType.SIMPLE_X:
            self.restriction_x = True
        if support_type == SupportType.SIMPLE_Y:
            self.restriction_y = True
        if support_type == SupportType.PINNED:
            self.restriction_x = True
            self.restriction_y = True
        if support_type == SupportType.FIXED:
            self.restriction_x = True
            self.restriction_y = True
            self.restriction_rot = True

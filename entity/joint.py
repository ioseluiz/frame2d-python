
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
    
  

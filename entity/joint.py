
class Joint():
    def __init__(self, id: int, x: float, y: float) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.restriction_x = False
        self.restriction_y = False
        self.restriction_rot = False
        self.degree_freedom = []
        self.assign_degree_freedom()
        
        
    def get_y(self) -> float:
        return self.y
    
    def get_x(self) -> float:
        return self.x
    
    def assign_degree_freedom(self):
        self.degree_freedom.append(3*self.id-2)
        self.degree_freedom.append(3*self.id-1)
        self.degree_freedom.append(3*self.id)
    
  

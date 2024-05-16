import math
import numpy as np
from entity.joint import Joint


class Frame():
    def __init__(self, id: int, start_joint: Joint, end_joint: Joint, mod_elast: float, inertia: float, area: float) -> None:
        self.id = id
        self.start_joint = start_joint
        self.end_joint = end_joint
        self.mod_elast = mod_elast
        self.inertia = inertia
        self.area = area
        self.length = self.calc_length()
        self.sin = self.calc_sin()
        self.cos = self.calc_cos()
        
        # Create Transform Matrix Loc to Global
        self.t_loc_glob = self.create_transform_mat_loc_glob()
        print("Transform Local to Global Matrix")
        print(self.t_loc_glob)
        # Create  Local stiffnes matrix K
        self.K_mat_loc = self.create_K_matrix_local()
        print("Local Matrix")
        print(self.K_mat_loc)
        # Create Global stiffnes matrix K
        self.K_mat_glob = self.transform_K_matrix_glob()
        print("Global Matrix")
        print(self.K_mat_glob)
        
    def calc_length(self) -> float:
        length = math.sqrt((self.end_joint.get_y() - self.start_joint.get_y())**2 + (self.end_joint.get_x() - self.start_joint.get_x())**2)
        return length
    
    def calc_sin(self):
        s = (self.end_joint.get_y() - self.start_joint.get_y()) / self.length
        return s
    
    def calc_cos(self):
        c = (self.end_joint.get_x() - self.start_joint.get_x()) / self.length
        return c
    
    def create_K_matrix_local(self):
        mat_k = np.zeros((6,6))
        # Coefficients
        # First Row
        mat_k[0,0] = self.mod_elast * self.area / self.length
        mat_k[3,0] = - self.mod_elast * self.area / self.length
        # Second Row
        mat_k[1,1] = (12 * self.mod_elast * self.inertia) / (self.length)**3
        mat_k[2,1] = (6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[4,1] = - (12 * self.mod_elast * self.inertia) / (self.length)**3
        mat_k[5,1] = (6 * self.mod_elast * self.inertia) / (self.length)**2
        # Third Row
        mat_k[1,2] = (6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[2,2] = (4 * self.mod_elast * self.inertia) / (self.length)
        mat_k[4,2] = - (6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[5,2] = (2 * self.mod_elast * self.inertia) / (self.length)
        # Fourth Row
        mat_k[0,3] = - self.mod_elast * self.area / self.length
        mat_k[3,3] = self.mod_elast * self.area / self.length
        # Fifth Row
        mat_k[1,4] = -(12 * self.mod_elast * self.inertia) / (self.length)**3
        mat_k[2,4] = -(6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[4,4] = (12 * self.mod_elast * self.inertia) / (self.length)**3
        mat_k[5,4] = -(6 * self.mod_elast * self.inertia) / (self.length)**2
        # Sixth Row
        mat_k[1,5] = (6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[2,5] = (2 * self.mod_elast * self.inertia) / (self.length)
        mat_k[4,5] = -(6 * self.mod_elast * self.inertia) / (self.length)**2
        mat_k[5,5] = (4 * self.mod_elast * self.inertia) / (self.length)
        
        return mat_k
        
    def create_transform_mat_loc_glob(self):
        mat_t= np.zeros((6,6))
        # First Row
        mat_t[0,0] = self.cos
        mat_t[1,0] = -self.sin
        # Second Row
        mat_t[0,1] = self.sin
        mat_t[1,1] = self.cos
        # Third Row
        mat_t[2,2] = 1
        # Fourth Row
        mat_t[3,3] = self.cos
        mat_t[4,3] = -self.sin
        # Fifth Row
        mat_t[3,4] = self.sin
        mat_t[4,4] = self.cos
        # Sixth Row
        mat_t[5,5] = 1
        
        return mat_t
    
    def transform_K_matrix_glob(self):
        return np.multiply(self.t_loc_glob, self.K_mat_loc)
        
        
    def __str__(self):
        return f"Frame: {self.id}, start joint: {self.start_joint.id} and end joint: {self.end_joint.id}. Length: {self.length}"
    
    
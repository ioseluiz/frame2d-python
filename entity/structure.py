import numpy as np
from entity.frame import Frame
from entity.frame import Joint

class Structure():
    def __init__(self, id: int, frames: list[Frame], joints: list[Joint]):
        self.id = id
        self.frames = frames # List of frames
        self.joints = joints # List of joints
        self.qty_joints = len(joints)
        self.degrees = 3*self.qty_joints
        self.K_global = self.calc_mat_K_global() #[K]

        # Displacement vector
        self.D_vector = [] # {D}
        self.F_vector = [] # {F}
        self.create_vectors_D_F()
        self.assign_D_vector()
        self.assign_restrictions()
        print(self.F_vector)
        print(self.D_vector)


        # Forces vector


        # Particular Solution Vector
        
    def calc_mat_K_global(self):
        mat_k = np.zeros((3*self.degrees,3*self.degrees))
        for frame in self.frames:
            print(f"----  Frame {frame.id} ----")
            print(frame.degrees_of_freedom)
            counter_i = 0
            for i in frame.degrees_of_freedom:
                counter_j = 0
                for j in frame.degrees_of_freedom:
                    mat_k[i-1][j-1] += frame.K_mat_glob[counter_i][counter_j]
                    counter_j += 1
                counter_i += 1
        return mat_k
      
    def assign_restrictions(self):
        for joint in self.joints:
            print(f"Joint {joint.id}")
            print(joint.restricted_degrees_freedom)
            if len(joint.restricted_degrees_freedom) > 0:
                for restriction in joint.restricted_degrees_freedom:
                    if restriction == 3*joint.id - 2:
                        self.F_vector[restriction - 1] = f"Rx{joint.id}"
                        self.D_vector[restriction - 1] = 0
                    if restriction == 3*joint.id - 1:
                        self.F_vector[restriction - 1] = f"Ry{joint.id}"
                        self.D_vector[restriction - 1] = 0
                    if restriction == 3*joint.id:
                        self.F_vector[restriction - 1] = f"M{joint.id}"
                        self.D_vector[restriction - 1] = 0

    def create_vectors_D_F(self):
        for i in range(0,3*len(self.joints)):
            self.F_vector.append(0)
            self.D_vector.append(0)

    def assign_D_vector(self):
        for joint in self.joints:
            self.D_vector[(3*joint.id-2)-1] = f"U{joint.id}"
            self.D_vector[(3*joint.id-1)-1] = f"V{joint.id}"
            self.D_vector[(3*joint.id)-1] = f"rot{joint.id}"




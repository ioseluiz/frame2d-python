import numpy as np
from entity.frame import Frame

class Structure():
    def __init__(self, id: int, frames: list[Frame], qty_joints: int):
        self.id = id
        self.frames = frames
        self.qty_joints = qty_joints
        self.degrees = 3*self.qty_joints
        self.calc_mat_K_global()
        


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
        np.set_printoptions(suppress=True)
        for i in range(15):
            print(f"Fila {i+1}")
            for j in range(15):
                print(mat_k[i][j])
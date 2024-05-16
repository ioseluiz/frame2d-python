from entity.joint import Joint
from entity.frame import Frame
from entity.structure import Structure

def main():
    #Sample Joints
    joint_1 = Joint(1, 0, 0)
    joint_2 = Joint(2, 0, 3)
    joint_3 = Joint(3, 6, 3)
    joint_4 = Joint(4, 6, 0)
    
    # Sample Frames
    frame_1 = Frame(1, joint_1, joint_2, 1, 1, 1)
    frame_2 = Frame(2, joint_2, joint_3, 1, 1, 1)
    frame_3 = Frame(3, joint_3, joint_4, 1, 1, 1)
    
    # Print
    frames = [frame_1, frame_2, frame_3]
    structure = Structure(1, frames)
    
if __name__ == "__main__":
    main()
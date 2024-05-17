from entity.joint import Joint
from entity.support import Support, SupportType
from entity.frame import Frame
from entity.structure import Structure

def main():
    #Sample Joints
    joint_1 = Joint(1, 0, 0)
    joint_2 = Joint(2, 0, 120)
    joint_3 = Joint(3, 240, 180)
    joint_4 = Joint(4, 480, 120)
    joint_5 = Joint(5, 480, 0)

    # Create Supports
    support_1 = Support(id=1,joint=joint_1,support_type=SupportType.FIXED)
    support_2 = Support(id=2, joint=joint_4, support_type=SupportType.FIXED)
    
    # Sample Frames
    frame_1 = Frame(1, joint_1, joint_2, 29000, 272, 14.4)
    frame_2 = Frame(2, joint_2, joint_3, 29000, 518, 11.8)
    frame_3 = Frame(3, joint_3, joint_4, 29000, 518, 11.8)
    frame_4 = Frame(4, joint_4, joint_5, 29000, 272, 14.4)
    
    # Print
    frames = [frame_1, frame_2, frame_3, frame_4]
    structure = Structure(1, frames, 5)
    
if __name__ == "__main__":
    main()
from joints import Joints


class Chains:
    Head = [Joints.HeadPitch, Joints.HeadYaw]
    LArm = [Joints.LShoulderRoll, Joints.LShoulderPitch, Joints.LElbowYaw,
            Joints.LElbowRoll, Joints.LWristYaw, Joints.LHand]
    RArm = [Joints.RShoulderRoll, Joints.RShoulderPitch, Joints.RElbowYaw,
            Joints.RElbowRoll, Joints.RWristYaw, Joints.RHand]
    LLeg = [Joints.LHipYawPitch, Joints.LHipPitch, Joints.LHipRoll,
            Joints.LKneePitch, Joints.LAnklePitch, Joints.LAnkleRoll]
    RLeg = [Joints.RHipPitch, Joints.RHipRoll, Joints.RKneePitch,
            Joints.RAnklePitch, Joints.RAnkleRoll]

    def __init__(self):
        pass

    @staticmethod
    def list():
        return [chain_name for chain_name in dir(Chains)
                if not (chain_name.startswith("__") or chain_name is 'list')]

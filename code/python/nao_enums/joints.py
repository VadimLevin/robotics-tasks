class Joints:
    # Head joints
    HeadPitch = "HeadPitch"
    HeadYaw = "HeadYaw"
    # Left arm joints
    LShoulderRoll = "LShoulderRoll"
    LShoulderPitch = "LShoulderPitch"
    LElbowYaw = "LElbowYaw"
    LElbowRoll = "LElbowRoll"
    LWristYaw = "LWristYaw"
    LHand = "LHand"
    # Right arm joints
    RShoulderRoll = "RShoulderRoll"
    RShoulderPitch = "RShoulderPitch"
    RElbowYaw = "RElbowYaw"
    RElbowRoll = "RElbowRoll"
    RWristYaw = "RWristYaw"
    RHand = "RHand"
    # Pelvis joints
    # LHipYawPitch and RHipYawPitch are physically just one motor so they
    # cannot be controlled independently.   In case of conflicting orders,
    # LHipYawPitch always takes the priority.
    LHipYawPitch = "LHipYawPitch"
    RHipYawPitch = "RHipYawPitch"
    # Left leg joints
    LHipPitch = "LHipPitch"
    LHipRoll = "LHipRoll"
    LKneePitch = "LKneePitch"
    LAnklePitch = "LAnklePitch"
    LAnkleRoll = "LAnkleRoll"
    # Right leg joints
    RHipRoll = "RHipRoll"
    RHipPitch = "RHipPitch"
    RKneePitch = "RKneePitch"
    RAnklePitch = "RAnklePitch"
    RAnkleRoll = "RAnkleRoll"

    def __init__(self):
        pass

    @staticmethod
    def list():
        return [joint_name for joint_name in dir(Joints)
                if not (joint_name.startswith("__") or joint_name is 'list')]

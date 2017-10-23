from nao_enums import Joints, Chains


ChainsJoints = {
    Chains.Head: [Joints.HeadPitch, Joints.HeadYaw],
    Chains.LArm: [Joints.LShoulderRoll, Joints.LShoulderPitch,
                  Joints.LElbowYaw, Joints.LElbowRoll, Joints.LWristYaw,
                  Joints.LHand],
    Chains.RArm: [Joints.RShoulderRoll, Joints.RShoulderPitch,
                  Joints.RElbowYaw, Joints.RElbowRoll, Joints.RWristYaw,
                  Joints.RHand],
    Chains.LLeg: [Joints.LHipYawPitch, Joints.LHipPitch, Joints.LHipRoll,
                  Joints.LKneePitch, Joints.LAnklePitch, Joints.LAnkleRoll],
    Chains.RLeg: [Joints.RHipPitch, Joints.RHipRoll, Joints.RKneePitch,
                  Joints.RAnklePitch, Joints.RAnkleRoll]
}

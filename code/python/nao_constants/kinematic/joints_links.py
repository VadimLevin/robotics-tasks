import numpy as np

from nao_enums import Chains


# Head
TORSO_HEAD_YAW = np.array([0., 0., 0.1265])
HEAD_YAW_HEAD_PITCH = np.array([0., 0., 0.])
# Left arm
L_TORSO_SHOULDER = np.array([0., 0.098, 0.1])
L_SHOULDER_ELBOW = np.array([0.105, 0.015, 0.])
L_ELBOW_WRIST = np.array([0.05595, 0., 0.])
L_WRIST_HAND = np.array([0.05775, 0., -0.01231])
# Right arm
R_TORSO_SHOULDER = np.array([0., -0.098, 0.1])
R_SHOULDER_ELBOW = np.array([0.105, -0.015, 0.])
R_ELBOW_WRIST = np.array([0.05595, 0., 0.])
R_WRIST_HAND = np.array([0.05775, 0., -0.01231])
# Left leg
L_TORSO_HIP = np.array([0., 0.05, -0.085])
L_HIP_KNEE = np.array([0., 0., -0.1])
L_KNEE_ANKLE = np.array([0., 0., -0.1029])
L_ANKLE_FOOT = np.array([0., 0., -0.04519])
# Right leg
R_TORSO_HIP = np.array([0., -0.05, -0.085])
R_HIP_KNEE = np.array([0., 0., -0.1])
R_KNEE_ANKLE = np.array([0., 0., -0.1029])
R_ANKLE_FOOT = np.array([0., 0., -0.04519])

JointsLinks = {
    Chains.Head: [TORSO_HEAD_YAW, HEAD_YAW_HEAD_PITCH],
    Chains.LArm: [L_TORSO_SHOULDER, L_SHOULDER_ELBOW, L_ELBOW_WRIST, L_WRIST_HAND],
    Chains.RArm: [R_TORSO_SHOULDER, R_SHOULDER_ELBOW, R_ELBOW_WRIST, R_WRIST_HAND],
    Chains.LLeg: [L_TORSO_HIP, L_HIP_KNEE, L_KNEE_ANKLE, L_ANKLE_FOOT],
    Chains.RLeg: [R_TORSO_HIP, R_HIP_KNEE, R_KNEE_ANKLE, R_ANKLE_FOOT]
}

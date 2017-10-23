from nao_enums import Chains
from nao_constants.kinematic import JointsLinks

from nao_alglib.math_extension import rotation_matrices as rot_mat
from nao_alglib.math_extension.projections import project_point_from_local_to_global_frame


def get_arm_position(arm_name, arm_angles):
    if arm_name not in [Chains.LArm, Chains.RArm]:
        raise ValueError("arm_name expected to be LArm or RArm. Got {0}".format(arm_name))
    shoulder_roll, shoulder_pitch, elbow_yaw, elbow_roll, wrist_yaw = arm_angles
    torso_shoulder, shoulder_elbow, elbow_wrist, wrist_hand = JointsLinks[arm_name]
    shoulder_rotation_mat = rot_mat.rotation_yz(shoulder_pitch, shoulder_roll)
    elbow_rotation_mat = rot_mat.rotation_xz(elbow_yaw, elbow_roll)
    wrist_rotation_mat = rot_mat.rotation_x(wrist_yaw)
    hand_in_elbow_crd_system = project_point_from_local_to_global_frame(wrist_rotation_mat,
                                                                        elbow_wrist,
                                                                        wrist_hand)
    hand_in_shoulder_crd_system = project_point_from_local_to_global_frame(elbow_rotation_mat,
                                                                           shoulder_elbow,
                                                                           hand_in_elbow_crd_system)
    return project_point_from_local_to_global_frame(shoulder_rotation_mat,
                                                    torso_shoulder,
                                                    hand_in_shoulder_crd_system)

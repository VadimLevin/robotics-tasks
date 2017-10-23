import numbers

from nao_enums import Joints, Chains
from nao_constants.kinematic import Constraints, ChainsJoints


def is_joint_inside_constraints(joint_name, joint_angle):
    if joint_name not in Joints.list():
        raise ValueError("joint_name must be one of the NAO joints. "
                         "Got {0}".format(joint_name)
                         )
    if not isinstance(joint_angle, numbers.Number):
        raise ValueError("Joint angle must be a number.")
    min_angle, max_angle = Constraints[joint_name]
    return min_angle <= joint_angle <= max_angle


def is_chain_inside_constraints(chain_name, chain_angles):
    if chain_name not in Chains.list():
        raise ValueError("chain_name must be one of the NAO chains")
    chain_joints = ChainsJoints[chain_name]
    if len(chain_angles) is not len(chain_joints):
        raise ValueError("chain_angles must have length {0},"
                         " got {1}".format(len(chain_joints),
                                           len(chain_angles))
                         )
    for joint, angle in zip(chain_joints, chain_angles):
        try:
            is_joint_fitted = is_joint_inside_constraints(joint, angle)
        except ValueError, value_err:
            print(value_err.message)
            is_joint_fitted = False
        if not is_joint_fitted:
            return False
    return True


def is_inside_constraints(chain_or_joint_name, angles):
    if chain_or_joint_name in Joints.list():
        return is_joint_inside_constraints(chain_or_joint_name, angles)
    else:
        return is_chain_inside_constraints(chain_or_joint_name, angles)

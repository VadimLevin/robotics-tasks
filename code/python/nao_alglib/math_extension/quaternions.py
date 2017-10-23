import numpy as np


def euler_angles_to_quaternion(euler_angles):
    cos_roll = np.cos(0.5 * euler_angles[0])
    sin_roll = np.sin(0.5 * euler_angles[0])
    cos_pitch = np.cos(0.5 * euler_angles[1])
    sin_pitch = np.sin(0.5 * euler_angles[1])
    cos_yaw = np.cos(0.5 * euler_angles[2])
    sin_yaw = np.sin(0.5 * euler_angles[2])
    qx = sin_roll * cos_pitch * cos_yaw - cos_roll * sin_pitch * sin_yaw
    qy = cos_roll * sin_pitch * cos_yaw + sin_roll * cos_pitch * sin_yaw
    qz = cos_roll * cos_pitch * sin_yaw - sin_roll * sin_pitch * cos_yaw
    qw = cos_roll * cos_pitch * cos_yaw + sin_roll * sin_pitch * sin_yaw
    quaternion = np.array([qx, qy, qz, qw])
    return quaternion / np.linalg.norm(quaternion)


def quaternion_to_euler_angles(quaternion):
    qx, qy, qz, qw = quaternion
    x_axis_rotation_angle = np.arctan2(2. * (qw * qx + qy * qz),
                                       1. - 2. * (qx ** 2 + qy ** 2))
    y_axis_rotation_angle = np.arcsin(2 * (qw * qy - qz * qx))
    z_axis_rotation_angle = np.arctan2(2. * (qw * qz + qx * qy),
                                       1. - 2. * (qy ** 2 + qz ** 2))
    return x_axis_rotation_angle, y_axis_rotation_angle, z_axis_rotation_angle


def axis_angle_to_quaternion(axis, angle):
    sin_half_angle = np.sin(0.5 * angle)
    cos_half_angle = np.cos(0.5 * angle)
    qx, qy = axis[0] * sin_half_angle, axis[1] * sin_half_angle
    if len(axis) == 3:
        qz = axis[2] * sin_half_angle
    else:
        return None
    qw = cos_half_angle
    quaternion = np.array([qx, qy, qz, qw])
    return quaternion / np.linalg.norm(quaternion)


def quaternion_to_rotation_matrix(quaternion, dimension):
    qx, qy, qz, qw = quaternion
    x_sq, y_sq, z_sq = qx ** 2, qy ** 2, qz ** 2
    xy, xz, xw = qx * qy, qx * qz, qx * qw
    yz, yw = qy * qz, qy * qw
    zw = qz * qw
    if dimension == 2:
        rotation_matrix = np.array([[1. - 2. * z_sq, -2. * zw],
                                    [2. * zw, 1. - 2. * z_sq]])
    elif dimension == 3:
        rotation_matrix = np.array([
            [1. - 2. * (y_sq + z_sq), 2. * (xy - zw), 2. * (xz + yw)],
            [2. * (xy + zw), 1. - 2. * (x_sq + z_sq), 2. * (yz - xw)],
            [2. * (xz - yw), 2. * (yz + xw), 1. - 2. * (x_sq + y_sq)]
        ])
    else:
        return None
    return rotation_matrix

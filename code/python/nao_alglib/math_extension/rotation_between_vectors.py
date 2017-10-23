import numpy as np
from quaternions import axis_angle_to_quaternion
from rotation_matrices import axis_angle_to_rotation_matrix


def axis_angle_rotation_between_vectors(in_from_vec, in_to_vec):
    dimension = len(in_from_vec)
    if dimension == 2:
        # Pad vectors to 3d dimension
        from_vec = np.pad(in_from_vec.copy(), (0, 1), 'constant',
                          constant_values=0)
        from_vec /= np.linalg.norm(from_vec)
        to_vec = np.pad(in_to_vec.copy(), (0, 1), 'constant',
                        constant_values=0)
        to_vec /= np.linalg.norm(to_vec)
    else:
        from_vec = in_from_vec.copy() / np.linalg.norm(in_from_vec)
        to_vec = in_to_vec.copy() / np.linalg.norm(in_to_vec)
    # Calculate the axis of the rotation
    cross_result = np.cross(from_vec, to_vec)
    cross_result_magnitude = np.linalg.norm(cross_result)
    if cross_result_magnitude > 0:
        axis_of_rotation = cross_result / cross_result_magnitude
    else:
        axis_of_rotation = np.array([0., 0., 1.])
    # Calculate the angle of the rotation
    # The dot product - cosine of the desired angle
    cos_angle = from_vec.dot(to_vec)
    if cos_angle < -1. or cos_angle > 1.:
        cos_angle = np.trunc(cos_angle)
    angle_of_rotation = np.arccos(cos_angle)
    return axis_of_rotation, angle_of_rotation


def rotation_matrix_between_vectors(in_from_vec, in_to_vec):
    axis, angle = axis_angle_rotation_between_vectors(in_from_vec, in_to_vec)
    return axis_angle_to_rotation_matrix(axis, angle)


def quaternion_rotation_between_vectors(in_from_vec, in_to_vec):
    axis, angle = axis_angle_rotation_between_vectors(in_from_vec, in_to_vec)
    return axis_angle_to_quaternion(axis, angle)

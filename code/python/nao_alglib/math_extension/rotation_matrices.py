import numpy as np


def rotation_x(angle):
    cos, sin = np.cos(angle), np.sin(angle)
    return np.array([
        [1., 0., 0.],
        [0., cos, -sin],
        [0., sin, cos]
    ])


def rotation_y(angle):
    cos, sin = np.cos(angle), np.sin(angle)
    return np.array([
        [cos, 0., sin],
        [0., 1, 0.],
        [-sin, 0, cos]
    ])


def rotation_z(angle):
    cos, sin = np.cos(angle), np.sin(angle)
    return np.array([
        [cos, -sin, 0.],
        [sin, cos, 0.],
        [0., 0., 1.]
    ])


def rotation_xy(x_angle, y_angle):
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    return np.array([
        [cos_y, 0., sin_y],
        [sin_x*sin_y, cos_x, -sin_x*cos_y],
        [-cos_x*sin_y, sin_x, cos_x*cos_y]
    ])


def rotation_xz(x_angle, z_angle):
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    return np.array([
        [cos_z, -sin_z, 0.],
        [cos_x*sin_z, cos_x*cos_z, -sin_x],
        [sin_x*sin_z, sin_x*cos_z, cos_x]
    ])


def rotation_yx(y_angle, x_angle):
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    return np.array([
        [cos_y, sin_y*sin_x, sin_y*cos_x],
        [0., cos_x, -sin_x],
        [-sin_y, cos_y*sin_x, cos_y*cos_x]
    ])


def rotation_yz(y_angle, z_angle):
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    return np.array([
        [cos_y*cos_z, -cos_y*sin_z, sin_y],
        [sin_z, cos_z, 0.],
        [-sin_y*cos_z, sin_y*sin_z, cos_y]
    ])


def rotation_zx(z_angle, x_angle):
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    return np.array([
        [cos_z, -sin_z*cos_x, sin_z*sin_x],
        [sin_z, cos_z*cos_x, -cos_z*sin_x],
        [0., sin_x, cos_x]
    ])


def rotation_zy(z_angle, y_angle):
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    return np.array([
        [cos_z*cos_y, -sin_z, cos_z*sin_y],
        [sin_z*cos_y, cos_z, sin_z*sin_y],
        [-sin_y, 0, cos_y]
    ])


def rotation_xyz(x_angle, y_angle, z_angle):
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    return np.array([
        [cos_y*cos_z, -cos_y*sin_z, sin_y],
        [sin_x*sin_y*cos_z + cos_x*sin_z, cos_x*cos_z - sin_x*sin_y*sin_z, -sin_x*cos_y],
        [sin_x*sin_z - cos_x*sin_y*cos_z, sin_x*cos_z + cos_x*sin_y*sin_z, cos_x*cos_y]

    ])


def rotation_xzy(x_angle, z_angle, y_angle):
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    return np.array([
        [cos_y*cos_z, -sin_z, sin_y*cos_z],
        [sin_x*sin_y + cos_x*cos_y*sin_z, cos_x*cos_z, cos_x*sin_y*sin_z - sin_x*cos_y],
        [sin_x*cos_y*sin_z - cos_x*sin_y, sin_x*cos_z, cos_x*cos_y + sin_x*sin_y*sin_z]
    ])


def rotation_yxz(y_angle, x_angle, z_angle):
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    return np.array([
        [cos_y*cos_z + sin_y*sin_x*sin_z, sin_y*sin_x*cos_z - cos_y*sin_z, sin_y*cos_x],
        [cos_x*sin_z, cos_x*cos_z, -sin_x],
        [cos_y*sin_x*sin_z - sin_y*cos_z, cos_y*sin_x*cos_z + sin_y*sin_z, cos_y*cos_x]
    ])


def rotation_yzx(y_angle, z_angle, x_angle):
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    return np.array([
        [cos_y*cos_z, sin_y*sin_x - cos_y*sin_z*cos_x, sin_y*cos_x + cos_y*sin_z*sin_x],
        [sin_z, cos_z*cos_x, -cos_z*sin_x],
        [-sin_y*cos_z, cos_y*sin_x + sin_y*sin_z*cos_x, cos_y*cos_x - sin_y*sin_z*sin_x]
    ])


def rotation_zxy(z_angle, x_angle, y_angle):
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    return np.array([
        [cos_z*cos_y - sin_z*sin_x*sin_x, -sin_z*cos_x, cos_z*sin_y + sin_z*sin_x*cos_y],
        [cos_z*sin_x*sin_y + sin_z*cos_y, cos_z*cos_x, sin_z*sin_y - cos_z*sin_x*cos_y],
        [-cos_x*sin_y, sin_x, cos_x*cos_y]
    ])


def rotation_zyx(z_angle, y_angle, x_angle):
    cos_z, sin_z = np.cos(z_angle), np.sin(z_angle)
    cos_y, sin_y = np.cos(y_angle), np.sin(y_angle)
    cos_x, sin_x = np.cos(x_angle), np.sin(x_angle)
    return np.array([
        [cos_z*cos_y, cos_z*sin_y*sin_x - sin_z*cos_x, cos_z*sin_y*cos_x + sin_z*sin_x],
        [sin_z*cos_y, cos_z*cos_x + sin_z*sin_y*sin_x, sin_z*sin_y*cos_x - cos_z*sin_x],
        [-sin_y, cos_y*sin_x, cos_y*cos_x]
    ])


def rotation_2d(angle, vector):
    cos, sin = np.cos(angle), np.sin(angle)
    x, y = vector
    return np.array([x*cos - y*sin, x*sin + y*cos])


def axis_angle_to_rotation_matrix(axis, angle):
    axis /= np.linalg.norm(axis)
    x, y, z = axis
    xy, xz, yz = x*y, x*z, y*z
    x_sq, y_sq, z_sq = x**2, y**2, z**2
    cos, sin = np.cos(angle), np.sin(angle)
    m_cos = 1. - cos
    return np.array([
        [cos + x_sq*m_cos, xy*m_cos - z*sin, xz*m_cos + y*sin],
        [xy*m_cos + z*sin, cos + y_sq*m_cos, yz*m_cos - x*sin],
        [xz*m_cos - y*sin, yz*m_cos + x*sin, cos + z_sq*m_cos]
    ])

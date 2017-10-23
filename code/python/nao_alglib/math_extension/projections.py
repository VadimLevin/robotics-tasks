
def project_point_from_global_to_local_frame(local_frame, local_frame_origin, point):
    return local_frame.transpose().dot(point - local_frame_origin)


def project_point_from_local_to_global_frame(local_frame, local_frame_origin, point):
    return local_frame.dot(point) + local_frame_origin

from nao_enums.joints import Joints

Constraints = {
    # Head joints constraints
    Joints.HeadPitch: [-0.6720, 0.5149],
    Joints.HeadYaw: [-2.0857, 2.0857],
    # Left arm constraints
    Joints.LShoulderRoll: [-0.3142, 1.3265],
    Joints.LShoulderPitch: [-2.0857, 2.0857],
    Joints.LElbowYaw: [-2.0857, 2.0857],
    Joints.LElbowRoll: [-1.5446, -0.0349],
    Joints.LWristYaw: [-1.8238, 1.8238],
    # Right arm constraints
    Joints.RShoulderRoll: [-1.3265, 0.3142],
    Joints.RShoulderPitch: [-2.0857, 2.0857],
    Joints.RElbowYaw: [-2.0857, 2.0857],
    Joints.RElbowRoll: [0.0349, 1.5446],
    Joints.RWristYaw: [-1.8238, 1.8238],
    # Pelvis constraints
    Joints.LHipYawPitch: [-1.145303, 0.740810],
    Joints.RHipYawPitch: [-1.145303, 0.740810],
    # Left leg constraints
    Joints.LHipPitch: [-1.535889, 0.484090],
    Joints.LHipRoll: [-0.379472, 0.790477],
    Joints.LKneePitch: [-0.092346, 2.112528],
    Joints.LAnklePitch: [1.189516, 0.922747],
    Joints.LAnkleRoll: [-0.397880, 0.769001],
    # Right leg constraints
    Joints.RHipPitch: [-1.535889, 0.484090],
    Joints.RHipRoll: [-0.790477, 0.379472],
    Joints.RKneePitch: [-0.103083, 2.120198],
    Joints.RAnklePitch: [-1.186448, 0.932056],
    Joints.RAnkleRoll: [0.768992, 0.397935]
}

# Pitch motion range is limited according to the Yaw value.
head_anti_collision_limitation = {  # HeadYaw: [HeadPitch_min HeadPitch_max]
                                    -2.086017: [-0.449073, 0.330041],
                                    -1.526988: [-0.330041, 0.200015],
                                    -1.089958: [-0.430049, 0.300022],
                                    -0.903033: [-0.479965, 0.330041],
                                    -0.756077: [-0.548033, 0.370010],
                                    -0.486074: [-0.671951, 0.422021],
                                    0.0000000: [-0.671951, 0.515047],
                                    0.486074: [-0.671951, 0.422021],
                                    0.756077: [-0.548033, 0.370010],
                                    0.903033: [-0.479965, 0.330041],
                                    1.089958: [-0.430049, 0.300022],
                                    1.526988: [-0.330041, 0.200015],
                                    2.086017: [-0.449073, 0.330041]}

# Due to potential shell collision at the ankle level, the Roll motion range
# is limited according to the Pitch value.

left_leg_anti_collision_limitation = {  # LAnklePitch: LAnkleRoll [Min, Max]
                                        -1.189442: [-0.049916, 0.075049],
                                        -0.840027: [-0.179943, 0.169995],
                                        -0.700051: [-0.397935, 0.220086],
                                        -0.449946: [-0.397935, 0.768992],
                                        0.100007: [-0.397935, 0.768992],
                                        0.349938: [-0.397935, 0.550477],
                                        0.922755: [0.0000000, 0.049916]}

# Due to potential shell collision at the ankle level, the Roll motion range
# is limited according to the Pitch value.
right_leg_anti_collision_limitation = {  # RAnklePitch: RAnkleRoll [Min, Max]
                                        -1.189442: [-0.075049, 0.049916],
                                        -0.840027: [-0.169995, 0.179943],
                                        -0.700051: [-0.220086, 0.397935],
                                        -0.449946: [-0.768992, 0.397935],
                                        0.100007: [-0.768992, 0.397935],
                                        0.349938: [-0.550477, 0.397935],
                                        0.922755: [-0.049916, 0.000000]}

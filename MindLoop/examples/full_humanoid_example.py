"""
Minimal Example: Full Humanoid Robot Structure
"""
from MindLoop.mindloop.nn import create_default_brain, MLP
from MindLoop.mindloop.effectors.anatomy.arm import Arm
from MindLoop.mindloop.effectors.anatomy.leg import Leg
from MindLoop.mindloop.effectors.anatomy.hand import Hand
from MindLoop.mindloop.effectors.anatomy.fingers import Finger
from MindLoop.mindloop.effectors.anatomy.foot import Foot
from MindLoop.mindloop.effectors.anatomy.spine import Spine
from MindLoop.mindloop.sensors.proprioception.joint_state import JointState
from MindLoop.mindloop.sensors.vision.camera import Camera
from MindLoop.mindloop.sensors.tactile.fingertip_array import FingertipArray
from MindLoop.mindloop.sensors.vestibular.imu import IMU
from MindLoop.mindloop.sensors.thermal.skin_temp import SkinTemp
import torch

# 1. Create brain
brain = create_default_brain()

# 2. Create body effectors
left_arm = Arm()
right_arm = Arm()
left_leg = Leg()
right_leg = Leg()
spine = Spine()
left_hand = Hand([Finger(name) for name in ['thumb', 'index', 'middle', 'ring', 'little']])
right_hand = Hand([Finger(name) for name in ['thumb', 'index', 'middle', 'ring', 'little']])
left_foot = Foot()
right_foot = Foot()

# 3. Create sensors
joint_state = JointState(['shoulder', 'elbow', 'wrist', 'hip', 'knee', 'ankle'])
camera = Camera()
tactile_left = FingertipArray(num_fingers=5)
tactile_right = FingertipArray(num_fingers=5)
imu = IMU()
skin_temp = SkinTemp()

# 4. Assign a model to MotorCortex for full body control
brain.components['MotorCortex'].model = MLP(input_dim=20, hidden_dim=64, output_dim=10)

# 5. Simulate a step: read sensors, generate command, move effectors
sensor_data = torch.randn(1, 20)  # e.g., vision + joint + tactile + imu + temp
command = brain.components['MotorCortex'].model(sensor_data).squeeze().tolist()

# 6. Move arms and legs (example: just use part of command vector)
left_arm.move({'shoulder': command[0], 'elbow': command[1], 'wrist': command[2]})
right_arm.move({'shoulder': command[3], 'elbow': command[4], 'wrist': command[5]})
left_leg.move({'hip': command[6], 'knee': command[7], 'ankle': command[8]})
right_leg.move({'hip': command[6], 'knee': command[7], 'ankle': command[8]})
spine.move(command[9:14])

# 7. Print out effector and sensor states
print("Left arm positions:", left_arm.positions)
print("Right arm positions:", right_arm.positions)
print("Left leg positions:", left_leg.positions)
print("Right leg positions:", right_leg.positions)
print("Spine positions:", spine.positions)
print("Camera image shape:", len(camera.read()), 'x', len(camera.read()[0]))
print("IMU:", imu.read())
print("Skin temp:", skin_temp.read()) 
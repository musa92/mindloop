"""
Minimal Example: Needle Sewing Task with Hand, Fingers, and Tactile Sensing
"""
from MindLoop.mindloop.nn import create_default_brain, MLP
from MindLoop.mindloop.effectors.anatomy.hand import Hand
from MindLoop.mindloop.effectors.anatomy.fingers import Finger
from MindLoop.mindloop.sensors.tactile.fingertip_array import FingertipArray
import torch

# 1. Create brain
brain = create_default_brain()

# 2. Create hand with fingers
fingers = [Finger(name) for name in ['thumb', 'index', 'middle', 'ring', 'little']]
hand = Hand(fingers)

# 3. Attach tactile sensor to fingertips
tactile = FingertipArray(num_fingers=5)

# 4. Assign a model to MotorCortex for fine control
brain.components['MotorCortex'].model = MLP(input_dim=10, hidden_dim=32, output_dim=5)

# 5. Simulate a step: generate dummy sensor data and command hand
sensor_data = torch.randn(1, 10)  # e.g., vision + tactile + proprioception
command = brain.components['MotorCortex'].model(sensor_data).squeeze().tolist()

# 6. Move each finger according to command
for i, finger in enumerate(hand.fingers):
    finger.move(command[i])
    tactile.set_touch(i, abs(command[i]))  # Simulate touch feedback

# 7. Print out finger positions and tactile readings
print("Finger positions:", [f.position for f in hand.fingers])
print("Tactile readings:", tactile.read()) 
class JointState:
    """Minimal proprioceptive sensor for joint positions."""
    def __init__(self, joints):
        self.joints = joints
        self.positions = {joint: 0.0 for joint in joints}

    def read(self):
        # Return current joint positions
        return self.positions

    def set_position(self, joint, value):
        self.positions[joint] = value

class Arm:
    """Minimal arm effector with joints."""
    def __init__(self, joints=None):
        self.joints = joints or ['shoulder', 'elbow', 'wrist']
        self.positions = {joint: 0.0 for joint in self.joints}

    def move(self, command):
        # Command is a dict {joint: position}
        for joint in self.joints:
            if joint in command:
                self.positions[joint] = command[joint]

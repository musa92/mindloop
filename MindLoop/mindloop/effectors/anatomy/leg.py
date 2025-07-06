class Leg:
    """Minimal leg effector with joints."""
    def __init__(self, joints=None):
        self.joints = joints or ['hip', 'knee', 'ankle']
        self.positions = {joint: 0.0 for joint in self.joints}

    def move(self, command):
        # Command is a dict {joint: position}
        for joint in self.joints:
            if joint in command:
                self.positions[joint] = command[joint]

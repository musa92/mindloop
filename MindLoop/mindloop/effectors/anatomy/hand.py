class Hand:
    """Minimal hand effector with attachable fingers."""
    def __init__(self, fingers=None):
        self.fingers = fingers or []

    def attach_finger(self, finger):
        self.fingers.append(finger)

    def move(self, command):
        # Command could be a dict or tensor specifying finger positions
        for finger in self.fingers:
            finger.move(command.get(finger.name, 0))

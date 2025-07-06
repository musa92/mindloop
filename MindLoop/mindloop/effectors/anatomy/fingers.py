class Finger:
    """Minimal finger effector for fine control."""
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, position):
        self.position = position

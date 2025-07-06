class Spine:
    """Minimal spine effector with segments."""
    def __init__(self, segments=5):
        self.segments = segments
        self.positions = [0.0] * segments

    def move(self, command):
        # Command is a list of positions for each segment
        for i in range(min(self.segments, len(command))):
            self.positions[i] = command[i]

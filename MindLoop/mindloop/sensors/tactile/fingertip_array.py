class FingertipArray:
    """Minimal tactile sensor array for fingertips."""
    def __init__(self, num_fingers=5):
        self.num_fingers = num_fingers
        self.touches = [0.0] * num_fingers

    def read(self):
        # Return current touch values (simulate or connect to hardware)
        return self.touches

    def set_touch(self, finger_idx, value):
        self.touches[finger_idx] = value

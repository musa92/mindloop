class IMU:
    """Minimal vestibular sensor (IMU for balance)."""
    def __init__(self):
        self.orientation = [0.0, 0.0, 0.0]  # roll, pitch, yaw
        self.acceleration = [0.0, 0.0, 0.0]

    def read(self):
        # Return current orientation and acceleration
        return {'orientation': self.orientation, 'acceleration': self.acceleration} 
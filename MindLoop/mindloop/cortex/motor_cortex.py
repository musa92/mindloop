class MotorCortex:
    """
    MotorCortex: Generates and coordinates motor commands for effectors using proportional control.
    Example:
        mc = MotorCortex(kp=0.5)
        action = mc.process({'target': 1.0, 'current': 0.2})
    """
    def __init__(self, kp: float = 0.5):
        self.kp = kp

    def process(self, sensor_data: dict) -> dict:
        """Compute motor command as proportional error correction."""
        target = sensor_data.get('target', 0.0)
        current = sensor_data.get('current', 0.0)
        command = self.kp * (target - current)
        return {'command': command}

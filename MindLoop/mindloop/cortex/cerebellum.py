class Cerebellum:
    """
    Cerebellum: Error correction and adaptive control using a simple PID-like update.
    Example:
        cb = Cerebellum(kp=0.5, ki=0.1, kd=0.05)
        corrected = cb.update({'command': 1.0}, {'error': 0.2})
    """
    def __init__(self, kp: float = 0.5, ki: float = 0.1, kd: float = 0.05):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, motor_command: dict, feedback: dict) -> dict:
        error = feedback.get('error', 0.0)
        self.integral += error
        derivative = error - self.prev_error
        self.prev_error = error
        correction = self.kp * error + self.ki * self.integral + self.kd * derivative
        return {'corrected_command': motor_command.get('command', 0.0) + correction}

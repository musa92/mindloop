class ReflexArc:
    """
    ReflexArc: Fast, automatic sensorimotor responses if a threshold is crossed.
    Example:
        ra = ReflexArc(threshold=0.5)
        response = ra.trigger({'touch': 0.7})
    """
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    def trigger(self, sensor_input: dict) -> dict:
        if sensor_input.get('touch', 0.0) > self.threshold:
            return {'reflex': 'withdraw'}
        return {'reflex': 'none'}

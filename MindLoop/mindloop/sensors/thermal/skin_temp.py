class SkinTemp:
    """Minimal thermal sensor for skin temperature."""
    def __init__(self):
        self.temperature = 36.5  # Default human skin temp in Celsius

    def read(self):
        return self.temperature 
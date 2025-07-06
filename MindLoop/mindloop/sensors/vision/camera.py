class Camera:
    """Minimal vision sensor (camera)."""
    def __init__(self, resolution=(64, 64)):
        self.resolution = resolution

    def read(self):
        # Return dummy image data (could be replaced with real camera input)
        return [[0]*self.resolution[1] for _ in range(self.resolution[0])]

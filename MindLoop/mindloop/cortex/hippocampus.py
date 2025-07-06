class Hippocampus:
    """
    Hippocampus: Memory and spatial navigation, storing sequences of events.
    Example:
        hc = Hippocampus()
        hc.remember('task', ['move', 'touch'])
        memory = hc.recall('task')
    """
    def __init__(self):
        self.memory = {}

    def remember(self, key: str, value: list) -> None:
        """Store a memory."""
        self.memory[key] = value

    def recall(self, key: str) -> list:
        """Recall a memory by key."""
        return self.memory.get(key, [])

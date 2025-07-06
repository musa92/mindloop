class Foot:
    """Minimal foot effector with toes."""
    def __init__(self, toes=None):
        self.toes = toes or ['big_toe', 'second_toe', 'third_toe', 'fourth_toe', 'little_toe']
        self.positions = {toe: 0.0 for toe in self.toes}

    def move(self, command):
        # Command is a dict {toe: position}
        for toe in self.toes:
            if toe in command:
                self.positions[toe] = command[toe]

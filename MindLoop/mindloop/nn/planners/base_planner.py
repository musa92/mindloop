class Planner:
    """Base class for robot task or trajectory planners."""
    def plan(self, state, goal):
        raise NotImplementedError 
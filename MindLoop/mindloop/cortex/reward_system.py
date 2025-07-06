class RewardSystem:
    """
    RewardSystem: Motivation and reinforcement learning, tracking cumulative reward.
    Example:
        rs = RewardSystem()
        rs.update(1.0)
        total = rs.total_reward
    """
    def __init__(self):
        self.total_reward = 0.0

    def update(self, reward: float) -> float:
        self.total_reward += reward
        return self.total_reward

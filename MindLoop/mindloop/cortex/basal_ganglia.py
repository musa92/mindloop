class BasalGanglia:
    """
    BasalGanglia: Action selection and habit learning by choosing the action with the highest reward.
    Example:
        bg = BasalGanglia()
        action = bg.select_action([{'name': 'move', 'reward': 1.0}, {'name': 'idle', 'reward': 0.2}], {})
    """
    def select_action(self, possible_actions: list, state: dict) -> str:
        if not possible_actions:
            return None
        best = max(possible_actions, key=lambda a: a.get('reward', 0.0))
        return best['name']

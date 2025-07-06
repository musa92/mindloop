class PrefrontalCortex:
    """
    PrefrontalCortex: High-level planning and decision making.
    Example:
        pfc = PrefrontalCortex()
        plan = pfc.plan('touch', {'object': 'button'})
    """
    def plan(self, goal: str, context: dict) -> list:
        """Plan a sequence of actions to achieve a goal."""
        if goal == 'touch' and 'object' in context:
            return [f"move_hand_to_{context['object']}", "extend_finger", "touch"]
        return ["idle"]

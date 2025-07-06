class BrainComponent:
    """Base class for a neural brain component."""
    def __init__(self, name: str, model=None):
        self.name = name
        self.model = model

    def train(self, data):
        if self.model is None:
            raise ValueError("No model assigned to component")
        # Placeholder: integrate with training engine
        pass


class MotorCortex(BrainComponent):
    """Motor cortex responsible for low level motor actions."""
    pass


class PrefrontalCortex(BrainComponent):
    """Prefrontal cortex handling high level planning."""
    pass


class BasalGanglia(BrainComponent):
    """Basal ganglia: action selection, habit formation, and procedural learning."""
    pass


class Cerebellum(BrainComponent):
    """Cerebellum: motor learning, coordination, and error correction."""
    pass


class Hippocampus(BrainComponent):
    """Hippocampus: memory formation, spatial navigation, and contextual learning."""
    pass


class RewardSystem(BrainComponent):
    """Reward system: motivation, reinforcement learning, and value-based decision making."""
    pass


class ReflexArc(BrainComponent):
    """Reflex arc: fast, automatic sensorimotor responses for immediate reactions."""
    pass


class Brain:
    """Container for brain components."""

    def __init__(self):
        self.components = {}

    def register(self, component_name: str, component: BrainComponent):
        self.components[component_name] = component

    def train_component(self, component_name: str, data):
        component = self.components.get(component_name)
        if not component:
            raise KeyError(f"Component {component_name} not found")
        component.train(data)


def create_default_brain():
    """
    Create a Brain instance with all major brain components registered.
    Returns:
        Brain: A brain with MotorCortex, PrefrontalCortex, BasalGanglia, Cerebellum, Hippocampus, RewardSystem, and ReflexArc.
    Example:
        brain = create_default_brain()
        brain.train_component('MotorCortex', data)
    """
    brain = Brain()
    brain.register('MotorCortex', MotorCortex('MotorCortex'))
    brain.register('PrefrontalCortex', PrefrontalCortex('PrefrontalCortex'))
    brain.register('BasalGanglia', BasalGanglia('BasalGanglia'))
    brain.register('Cerebellum', Cerebellum('Cerebellum'))
    brain.register('Hippocampus', Hippocampus('Hippocampus'))
    brain.register('RewardSystem', RewardSystem('RewardSystem'))
    brain.register('ReflexArc', ReflexArc('ReflexArc'))
    return brain

from .motor_cortex import MotorCortex
from .prefrontal import PrefrontalCortex
from .cerebellum import Cerebellum
from .basal_ganglia import BasalGanglia
from .hippocampus import Hippocampus
from .reward_system import RewardSystem
from .reflex_arc import ReflexArc

class Cortex:
    """
    Cortex orchestrator: wires up all cortex regions and manages the full perception-to-action loop.
    Example:
        cortex = Cortex()
        result = cortex.run_step(goal='touch', context={'object': 'button'}, sensor_data={'target': 1.0, 'current': 0.2, 'touch': 0.7})
    """
    def __init__(self):
        self.prefrontal = PrefrontalCortex()
        self.basal_ganglia = BasalGanglia()
        self.motor = MotorCortex()
        self.cerebellum = Cerebellum()
        self.hippocampus = Hippocampus()
        self.reward_system = RewardSystem()
        self.reflex_arc = ReflexArc()

    def run_step(self, goal: str, context: dict, sensor_data: dict) -> dict:
        # 1. Plan
        plan = self.prefrontal.plan(goal, context)
        self.hippocampus.remember('last_plan', plan)
        # 2. Action selection
        possible_actions = [{'name': act, 'reward': 1.0 if act == 'touch' else 0.5} for act in plan]
        action = self.basal_ganglia.select_action(possible_actions, context)
        self.hippocampus.remember('last_action', [action])
        # 3. Motor command
        motor_cmd = self.motor.process(sensor_data)
        # 4. Error correction
        feedback = {'error': sensor_data.get('target', 0.0) - sensor_data.get('current', 0.0)}
        corrected = self.cerebellum.update(motor_cmd, feedback)
        # 5. Reflex
        reflex = self.reflex_arc.trigger(sensor_data)
        # 6. Reward
        reward = 1.0 if action == 'touch' else 0.0
        total_reward = self.reward_system.update(reward)
        # 7. Return all results
        return {
            'plan': plan,
            'selected_action': action,
            'motor_command': motor_cmd,
            'corrected_command': corrected,
            'reflex': reflex,
            'reward': reward,
            'total_reward': total_reward,
            'memory': self.hippocampus.memory
        } 
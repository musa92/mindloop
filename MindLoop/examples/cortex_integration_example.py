"""
Cortex Integration Example: Simulate a perception-to-action loop for a 'touch' task.
"""
from MindLoop.mindloop.cortex.cortex import Cortex

# 1. Create the cortex orchestrator
cortex = Cortex()

# 2. Define a goal, context, and sensor data
goal = 'touch'
context = {'object': 'button'}
sensor_data = {'target': 1.0, 'current': 0.2, 'touch': 0.7}

# 3. Run a cortex step
result = cortex.run_step(goal, context, sensor_data)

# 4. Print all outputs
print("Cortex Step Result:")
for k, v in result.items():
    print(f"{k}: {v}") 
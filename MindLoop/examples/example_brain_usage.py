"""
Minimal Example: Task-based Humanoid Robot Brain
"""
from MindLoop.mindloop.nn import create_default_brain, MLP
import torch

# 1. Create a brain with all components
brain = create_default_brain()

# 2. Assign a simple MLP model to the MotorCortex
brain.components['MotorCortex'].model = MLP(input_dim=5, hidden_dim=16, output_dim=2)

# 3. Dummy data for training (replace with real data as needed)
dummy_data = torch.randn(10, 5)  # 10 samples, 5 features each

# 4. Train the MotorCortex component (will not error now)
brain.train_component('MotorCortex', dummy_data)

# 5. List registered components
print("Registered brain components:", list(brain.components.keys())) 
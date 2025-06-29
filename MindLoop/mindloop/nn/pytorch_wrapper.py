import torch
import math

# -----------------------------------
# Tensor Memory & Conversion Utilities
# -----------------------------------

def allocate(shape, dtype=torch.float32, device='cpu', pin=False):
    return torch.empty(shape, dtype=dtype, device=device, pin_memory=pin)

def to_tensor(x, dtype=torch.float32, device='cpu'):
    return torch.tensor(x, dtype=dtype, device=device)

def move_to_device(data, device):
    if isinstance(data, dict):
        return {k: move_to_device(v, device) for k, v in data.items()}
    elif isinstance(data, list):
        return [move_to_device(x, device) for x in data]
    elif isinstance(data, torch.Tensor):
        return data.to(device)
    return data

# -----------------------------------
# Control & Reflex Systems (Motor Cortex)
# -----------------------------------

def pid(setpoint, measured, prev_error, integral, dt, kp, ki=0.0, kd=0.0):
    error = setpoint - measured
    derivative = (error - prev_error) / dt
    integral = integral + error * dt
    output = kp * error + ki * integral + kd * derivative
    return output, error, integral

def clamp_tensor(tensor, min_val, max_val):
    return torch.clamp(tensor, min_val, max_val)

def motion_plan(current, goal, max_step=0.1):
    delta = goal - current
    step = delta.clamp(-max_step, max_step)
    return current + step

def motor_habituation(output, decay=0.01):
    return output * (1 - decay)

def adaptive_gain(error, baseline=0.1, alpha=0.5):
    return alpha * torch.abs(error) + baseline

def bang_bang_control(setpoint, measurement):
    return torch.sign(setpoint - measurement)

def center_of_mass(joint_positions, masses):
    return torch.sum(joint_positions * masses[:, None], dim=0) / torch.sum(masses)

def balance_stabilizer(com, base, stiffness=1.0):
    return stiffness * (base - com)

# -----------------------------------
# Vision & Spatial Geometry (Occipital & Parietal Cortex)
# -----------------------------------

def normalize_angle(theta):
    return ((theta + math.pi) % (2 * math.pi)) - math.pi

def angle_diff(a, b):
    return normalize_angle(a - b)

def project_to_image(x3d, K):
    fx, fy, cx, cy = K
    x, y, z = x3d[..., 0], x3d[..., 1], x3d[..., 2]
    u = fx * x / z + cx
    v = fy * y / z + cy
    return torch.stack([u, v], dim=-1)

def depth_map_to_pointcloud(depth_tensor, fx, fy, cx, cy):
    B, H, W = depth_tensor.shape
    y, x = torch.meshgrid(torch.arange(H), torch.arange(W), indexing='ij')
    x = (x - cx) / fx
    y = (y - cy) / fy
    z = depth_tensor
    x3 = x * z
    y3 = y * z
    return torch.stack([x3, y3, z], dim=-1)

def rhythmic_signal(t, freq=1.0, amp=1.0, phase=0.0):
    return amp * torch.sin(2 * math.pi * freq * t + phase)

def entrain_cycle(signal, target_freq, phase_offset=0.0):
    return torch.sin(2 * math.pi * target_freq * signal + phase_offset)

# -----------------------------------
# Filtering & Estimation (Cerebellum)
# -----------------------------------

def kalman_1d(z, x_est, p_est, A, B, H, Q, R, u):
    x_pred = A * x_est + B * u
    p_pred = A * p_est * A + Q
    K = p_pred * H / (H * p_pred * H + R)
    x_upd = x_pred + K * (z - H * x_pred)
    p_upd = (1 - K * H) * p_pred
    return x_upd, p_upd

def ema_filter(current, previous, alpha=0.9):
    return alpha * previous + (1 - alpha) * current

def low_pass_filter(signal, prev, alpha):
    return alpha * signal + (1 - alpha) * prev

def bias_correction(sensor, bias):
    return sensor - bias

def reward_based_update(value, reward, lr=0.01):
    return value + lr * (reward - value)

def eligibility_trace(prev_trace, gradient, decay=0.9):
    return decay * prev_trace + gradient

# -----------------------------------
# Reflex Arcs & Sensorimotor Integration (Spinal Cord)
# -----------------------------------

def reflex_arc(sensor_input, threshold, gain=1.0):
    return torch.where(sensor_input > threshold, gain * sensor_input, torch.zeros_like(sensor_input))

def inhibit(signal, gate):
    return signal * (1 - gate)

def activate(signal, threshold=0.5):
    return (signal > threshold).float()

def spike(signal, gain=10.0):
    return torch.tanh(gain * signal)

def joint_limit_avoidance(joints, lower_bounds, upper_bounds, margin=0.05):
    return torch.clamp(joints, lower_bounds + margin, upper_bounds - margin)

def posture_alignment(joint_angles, desired_posture, gain=0.1):
    return joint_angles + gain * (desired_posture - joint_angles)

# -----------------------------------
# Cognitive Gating & Prioritization (Prefrontal Cortex)
# -----------------------------------

def attention_gate(inputs, weights):
    scores = torch.softmax(weights, dim=-1)
    return torch.sum(scores * inputs, dim=-1, keepdim=True)

def decision_softmax(logits, temperature=1.0):
    return torch.softmax(logits / temperature, dim=-1)

def delay_line(signal, history, steps=1):
    history.append(signal)
    if len(history) > steps:
        return history[-steps]
    return history[0]

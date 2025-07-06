import torch

def one_hot_encode(indices, num_classes):
    """One-hot encode a list or tensor of indices."""
    indices = torch.as_tensor(indices, dtype=torch.long)
    return torch.nn.functional.one_hot(indices, num_classes=num_classes) 
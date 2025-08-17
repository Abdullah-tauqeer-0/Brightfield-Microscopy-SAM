from segment_anything import sam_model_registry
import torch

def build_sam(model_type="vit_b", checkpoint=None):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    sam = sam_model_registry[model_type](checkpoint=checkpoint)
    sam.to(device)
    return sam

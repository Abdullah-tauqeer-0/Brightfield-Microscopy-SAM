import torch.nn as nn

class BrightfieldSAM(nn.Module):
    def __init__(self, sam_model):
        super().__init__()
        self.sam = sam_model
        # Add custom adapter layers here if needed
        
    def forward(self, x):
        return self.sam.image_encoder(x)

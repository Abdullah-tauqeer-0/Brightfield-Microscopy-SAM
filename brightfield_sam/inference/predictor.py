from segment_anything import SamPredictor
from ..utils.image import normalize_brightfield

class BrightfieldPredictor:
    def __init__(self, sam_model):
        self.predictor = SamPredictor(sam_model)
        
    def set_image(self, image):
        processed = normalize_brightfield(image)
        self.predictor.set_image(processed)
        
    def predict(self, point_coords=None, point_labels=None, box=None):
        masks, scores, logits = self.predictor.predict(
            point_coords=point_coords,
            point_labels=point_labels,
            box=box,
            multimask_output=True,
        )
        return masks

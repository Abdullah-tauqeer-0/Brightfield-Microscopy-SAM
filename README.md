# Brightfield Microscopy SAM

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

A specialized version of the Segment Anything Model (SAM) fine-tuned and optimized for brightfield microscopy images.

## 🌟 Features
- **Domain Adaptation:** Custom adapters for H&E and Phase Contrast images.
- **Napari Plugin:** Interactive annotation tool integrated with Napari.
- **Tiling Support:** Handle large Whole Slide Images (WSIs) seamlessly.
- **Fine-tuning API:** Easy-to-use trainer for custom datasets.

## 📦 Installation
```bash
pip install brightfield-sam
```

## 🚀 Usage
```python
from brightfield_sam.models import build_sam
from brightfield_sam.inference import BrightfieldPredictor

model = build_sam(model_type="vit_b")
predictor = BrightfieldPredictor(model)
predictor.set_image(image)
masks = predictor.predict(box=[100, 100, 200, 200])
```

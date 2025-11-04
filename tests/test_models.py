import unittest
import torch
from brightfield_sam.models.build import build_sam

class TestModels(unittest.TestCase):
    def test_build_sam(self):
        model = build_sam(model_type="vit_b")
        self.assertIsNotNone(model)
        
if __name__ == '__main__':
    unittest.main()

import unittest
import numpy as np
from brightfield_sam.utils.image import normalize_brightfield

class TestUtils(unittest.TestCase):
    def test_normalization(self):
        img = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        norm = normalize_brightfield(img)
        self.assertEqual(norm.shape, img.shape)

if __name__ == '__main__':
    unittest.main()

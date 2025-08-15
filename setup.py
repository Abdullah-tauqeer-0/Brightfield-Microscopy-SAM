from setuptools import setup, find_packages

setup(
    name="brightfield_sam",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
        "segment-anything",
        "numpy",
        "opencv-python",
        "napari",
        "magicgui",
        "qtpy"
    ],
    author="Abdullah Tauqeer",
    description="SAM for Brightfield Microscopy",
)

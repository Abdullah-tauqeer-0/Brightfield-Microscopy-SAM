import napari
from magicgui import magic_factory
from ..inference.predictor import BrightfieldPredictor

@magic_factory
def segment_widget(image: "napari.types.ImageData") -> "napari.types.LabelsData":
    # Napari widget logic
    return None

def launch_gui():
    viewer = napari.Viewer()
    viewer.window.add_dock_widget(segment_widget)
    napari.run()

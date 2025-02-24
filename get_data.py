from roboflow import Roboflow

rf = Roboflow(api_key="5VAwQF4VLN4j2HdLddRd")
project = rf.workspace("identification-pittin-corrosion").project("corrosion-segmentation-rsfbe")
version = project.version(24)
dataset = version.download("yolov8")
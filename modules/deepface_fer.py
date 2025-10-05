import os
import logging

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

logging.getLogger("tensorflow").setLevel(logging.ERROR)

from deepface.models.demography.Emotion import EmotionClient
from deepface import DeepFace
from rich import print

WEIGHTS_DIR = "assets/.deepface/weights/"
os.makedirs(WEIGHTS_DIR, exist_ok=True)

os.environ["DEEPFACE_HOME"] = "assets/"

class DeepFaceFer:
    def __init__(self):
        self.model = EmotionClient
        print(f"[bright_green][INFO][/] Successful loaded 'Emotion' model.")

    def EmotionRecognize(self, img):
        img_path = img['img_path']
        emotion  = img['emotion']

        if not os.path.exists(img_path):
            print(f"[bright_red][ERROR] Failed to find image path. [/]")
            return
        
        result_detect = {}
        result_detect['model_name'] = 'deepface'
        result_detect['dominant']   = None
        result_detect['percent']    = 0.0
        
        result = DeepFace.analyze(
            img_path=img_path,
            actions=['emotion'],
            enforce_detection=False
        )

        result_detect['dominant'] = result[0]['dominant_emotion']
        result_detect['percent']  = result[0]['emotion'][result_detect['dominant']]
        print(f"[bright_green][INFO][/] [bright_yellow]Result: {emotion} [ {result_detect['dominant']}: {result_detect['percent']} ][/]")

        return result_detect
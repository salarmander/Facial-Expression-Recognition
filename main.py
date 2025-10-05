from modules.deepface_fer import DeepFaceFer
from modules.get_images import getImages
from support_benchmark.support_benchmark import support_benchmark
from support_benchmark.accuracy import print_accuracy
from rich import print

def get_images():
    return getImages()

emo_detector = None
def init():
    global emo_detector
    emo_detector = DeepFaceFer()

def thread_processor():
    
    img = get_images()
    if not img:
        support_benchmark(None, img)
        return None
    
    deepface_result = emo_detector.EmotionRecognize(img)
    support_benchmark(deepface_result, img)

    return True

if __name__ == "__main__":
    print(f"[bright_green][INFO][/] [bright_yellow]BEGIN PROCESSING...[/]")

    init()
    while True:
        if not thread_processor():
            break

    print(f"[bright_green][INFO][/] [bright_yellow]END PROCESSING![/]")
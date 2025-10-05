from pathlib import Path
from rich import print

import os

INPUT_PATH = 'data/inputs/temp/'

COUNT = -1
def getImages():
    
    if not os.path.exists(INPUT_PATH):
        print(f"[bright_red][ERROR][/] Failed to access {INPUT_PATH}")
        return
    
    global COUNT
    result_img = {}
    result_img['file_name'] = None
    result_img['emotion']   = None
    result_img['img_path']  = None

    image_files = []
    root = Path(INPUT_PATH)
    for file in root.rglob("*.jpg"):
        image_files.append(file.as_posix())
    
    COUNT += 1
    if COUNT >= len(image_files):
        COUNT = 0
        return
    
    image_path = image_files[COUNT]
    result_img['img_path']   = image_path
    result_img['file_name']  = str(image_path).split('/')[4]
    result_img['emotion']    = str(image_path).split('/')[3]

    print(f"[bright_green][INFO][/] Current image: [bright_cyan]{result_img['emotion']}/{result_img['file_name']}[/]")
    
    return result_img
    
if __name__ == '__main__':
    _, _, img = getImages()
    print(img)
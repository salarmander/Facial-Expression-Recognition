from rich import print

accuracy = {}
accuracy['overall']  = {'count': 0, 'correct' : 0}
accuracy['angry']    = {'count': 0, 'correct' : 0}
accuracy['disgust']  = {'count': 0, 'correct' : 0}
accuracy['fear']     = {'count': 0, 'correct' : 0}
accuracy['happy']    = {'count': 0, 'correct' : 0}
accuracy['neutral']  = {'count': 0, 'correct' : 0}
accuracy['sad']      = {'count': 0, 'correct' : 0}
accuracy['surprise'] = {'count': 0, 'correct' : 0}

def get_accuracy_data(result, img):
    global accuracy 
    
    dominant = result['dominant']
    emotion  = img['emotion']

    accuracy['overall']['count'] += 1
    accuracy[emotion]['count']  += 1

    if str(dominant).lower() == str(emotion).lower():
        accuracy['overall']['correct'] += 1
        accuracy[dominant]['correct']  += 1

def calculate_accuracy():
    global accuracy

    accuracy_result = {}
    for emo, detail in accuracy.items():
        if detail['count'] == 0:
            detail['count'] = 1
        accuracy_result[emo] = float(detail['correct']/detail['count']) * 100

    return accuracy_result

def print_accuracy():
    global accuracy
    result = calculate_accuracy()

    for emo, detail in accuracy.items():
        print(f"[salmon1][DEBUG] {emo}: {detail} [/]")
    
    for emo, detail in result.items():
        print(f"[bright_green][INFO] {emo} : {detail}% [/]")
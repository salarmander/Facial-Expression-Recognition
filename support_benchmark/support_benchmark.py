from support_benchmark.export_excel import ExportToExcel
from support_benchmark.accuracy import calculate_accuracy, get_accuracy_data, print_accuracy
from rich import print

import os
import shutil

BENCHMARK_PATH = 'data/outputs/Benchmark/'

is_remove_first = True
def excel_output(result):
    model_name = result['model_name']
    path = f"{BENCHMARK_PATH}{model_name}"

    global is_remove_first
    if is_remove_first:
        try:
            shutil.rmtree(path)
        except OSError as error:
            print(f"[bright_red][ERROR] {error}[/] ")
        is_remove_first = False

    if not os.path.exists(path):
        os.makedirs(path)

report = None
def support_benchmark(result, img):

    global is_remove_first
    global report
    if is_remove_first:
        excel_output(result)
        model_name = result['model_name']
        file_path = f"{BENCHMARK_PATH}{model_name}/deepface_report.xlsx"
        report = ExportToExcel(file_path)

    if result and img:
        get_accuracy_data(result, img)
        report.export(result, img)
    
    if result is None and not img:
        result_accuracy = calculate_accuracy()
        report.export_accuracy(result_accuracy)
        print_accuracy()


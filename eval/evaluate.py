import json

from compile import *

code_file_names = {
    "c32" : "main.c",
    "c64" : "main.c",
    "c++32": "main.cpp",
    "c++64": "main.cpp" 
}



file_submission_data = open("submission_data.json")

submission_data = json.load(file_submission_data)



if not submission_data["compiler_type"] in code_file_names.keys():
    print("N-am gasit limbajul")
    exit()

code_file_name = code_file_names[submission_data["compiler_type"]]

compile(code_file_name, submission_data["compiler_type"])
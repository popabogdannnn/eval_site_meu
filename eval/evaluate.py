import os
from compile import *
from auxiliary_functions import *

code_file_names = {
    "c32" : "main.c",
    "c64" : "main.c",
    "c++32": "main.cpp",
    "c++64": "main.cpp" 
}

executable_file_name = "main"


submission_data = read_json("submission_data.json")



if not submission_data["compiler_type"] in code_file_names.keys():
    print("N-am gasit limbajul")
    exit()

code_file_name = code_file_names[submission_data["compiler_type"]]

compilation_result = compile(code_file_name, executable_file_name, submission_data["compiler_type"], submission_data["execution_time"], submission_data["memory"], submission_data["stack_memory"])

io_filename = submission_data["io_filename"]

test_lines = read_file("tests/tests.txt").split("\n")

for x in range(len(test_lines)):
    pass

os.system("rm " + code_file_name)
os.system("rm " + executable_file_name)


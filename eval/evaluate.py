import os
from compile import *
from run_sandbox import *
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
stdio = submission_data["stdio"]
io_filename = submission_data["io_filename"]
memory = submission_data["memory"]
stack_memory = submission_data["stack_memory"]
execution_time = submission_data["execution_time"]

compilation_result = compile(code_file_name, executable_file_name, submission_data["compiler_type"], submission_data["execution_time"], submission_data["memory"], submission_data["stack_memory"])

print(compilation_result)

test_lines = read_file("tests/tests.txt").split("\n")

for line in test_lines:
    line = line.split(' ')
    tag = line[0]
    points = int(line[1])

    in_file_tests = tag + "-" + io_filename + ".in"
    ok_file_tests = tag + "-" + io_filename + ".ok"
    in_file = io_filename + ".in"
    out_file = io_filename + ".out"
    
    os.system("rm -rf " + EXECUTION_JAIL +"/*")
    os.system("cp tests/" + in_file_tests + " " + EXECUTION_JAIL + "/" + in_file)
    os.system("echo -n > " + EXECUTION_JAIL + "/" + out_file)
    os.system("cp " + executable_file_name + " " + EXECUTION_JAIL +"/")

    run_snadbox(executable_file_name, stdio, memory, stack_memory, execution_time, in_file, out_file)

 

#os.system("rm " + code_file_name)
#if compilation_result["result"] == "success":
#    os.system("rm " + executable_file_name)


import os
from auxiliary_functions import *

COMPILE_MEMORY = 128 #in megabytes
COMPILE_TIME = 10 #in seconds
COMPILE_WALL_TIME = COMPILE_TIME + 2 #in seconds

compiler_commands = {
    "c32": "",
    "c64": "",
    "c++32": "",
    "c++64": "usr/bin/g++ -- -m64 -Wall -O2 -static -std=c++14 main.cpp -o main -lm"
}

compiler_dependencies = {
    "c32": [],
    "c64": [],
    "c++32": [],
    "c++64": ['/lib:/lib:exec',
              '/lib64:/lib64:exec',
                        '/usr/bin:/usr/bin:exec',
                        '/usr/lib:/usr/lib:exec',
                        '/usr/include:/usr/include']
}


def compile(code_file_name, executable_file_name,compiler_type, execution_time, memory, stack_memory):
    compile_command = compiler_commands[compiler_type]
    compiler_depency = compiler_dependencies[compiler_type]

    #os.system("rmdir /sys/fs/cgroup/cpuacct/ia-sandbox/default")
    os.system("rm -rf compilation_jail/*")
    os.system("cp " + code_file_name + " compilation_jail/")
    sandbox_command = "ia-sandbox -r /media/bogdan/0C4E0E4A4E0E2CD0/work/Linux/cpp/eval_site_meu/eval/compilation_jail --forward-env"

    for mount in compiler_depency:
        sandbox_command += " --mount " + mount
    
    sandbox_command += " --memory " + str(COMPILE_MEMORY) + "mb"
    sandbox_command += " --stack " + str(COMPILE_MEMORY) + "mb"
    sandbox_command += " --time " + str(COMPILE_TIME) + "s"
    sandbox_command += " --wall-time " + str(COMPILE_TIME + 2) + "s"
    sandbox_command += " --stderr compile_warnings"
    sandbox_command += " -o json"
    sandbox_command += " " + compile_command
    sandbox_command = "(" + sandbox_command + ") > compilation_data.json"
    
    os.system(sandbox_command)
    
    compilation_data = read_json("compilation_data.json")

    ret = {
        "result" : "fail",
        "warnings" : read_file("compile_warnings") 
    }

    os.system("rm compilation_data.json")
    os.system("rm compile_warnings")

    if "Success" in compilation_data["result"].keys():
        os.system("mv compilation_jail/" + executable_file_name + " ./")
        ret["result"] = "success"
    return ret
    
    


    
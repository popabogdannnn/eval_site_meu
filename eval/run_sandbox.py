import os
from auxiliary_functions import *

def run_sandbox(executable_file_name, stdio, memory, stack_memory, execution_time, in_file, out_file):
   
    os.system("rmdir /sys/fs/cgroup/memory/ia-sandbox/default/isolated")
    os.system("rmdir /sys/fs/cgroup/memory/ia-sandbox/default")

    sandbox_command = "ia-sandbox -r " + PWD + "/" + EXECUTION_JAIL

    if stdio: 
        sandbox_command += " --stdin " + in_file
        sandbox_command += " --stdout " + out_file
    
    sandbox_command += " --memory " + str(memory) + "kb"
    sandbox_command += " --stack " + str(stack_memory) + "kb"
    sandbox_command += " --time " + str(execution_time) + "ms"
    sandbox_command += " --wall-time " + str(execution_time + 2000) + "ms"
    sandbox_command += " --stderr execution_stderr"
    sandbox_command += " -o json"
    sandbox_command += " ./" + executable_file_name
    sandbox_command = "(" + sandbox_command + ") > execution_data.json" 

    os.system(sandbox_command)

    ret = {
    
    }

    execution_data = read_json("execution_data.json")
    
    ret = copy.deepcopy(execution_data)
    del ret["usage"]["wall_time"]
    
    ret["stderr"] = read_file("execution_stderr")

    os.system("rm execution_stderr")
    os.system("rm execution_data.json")

    return ret



    
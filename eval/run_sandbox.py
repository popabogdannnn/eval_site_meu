import os
from auxiliary_functions import *

def run_snadbox(executable_file_name, stdio, memory, stack_memory, execution_time, in_file, out_file):
    sandbox_command = "ia-sandbox -r /media/bogdan/0C4E0E4A4E0E2CD0/work/Linux/cpp/eval_site_meu/eval/execution_jail"
    
    if stdio: 
        sandbox_command += " --stdin " + in_file
        sandbox_command += " --stdout " + out_file
    
    sandbox_command += " --memory " + str(memory) + "kb"
    sandbox_command += " --stack " + str(stack_memory) + "kb"
    sandbox_command += " --time " + str(execution_time) + "ms"
    sandbox_command += " --wall-time " + str(execution_time + 2000) + "ms"
    sandbox_command += " --stderr execution_stderr"
    sandbox_command += " -o oneline"
    sandbox_command += " ./" + executable_file_name
    sandbox_command = "(" + sandbox_command + ") > execution_data.json" 

    #print(sandbox_command)
    os.system(sandbox_command)

    
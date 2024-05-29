from subprocess import run
import json


def get_kernel():
    return(run(["uname", "-r"], capture_output=True, text=True).stdout.strip())

def get_uptime():
    return(run(["uptime"], capture_output=True, text=True).stdout.strip().split(',')[0])

def get_cpu_usage():
    output = json.loads(run(["mpstat", "-o", "JSON"], capture_output=True, text=True).stdout)
    return output['sysstat']['hosts'][0]['statistics'][0]['cpu-load'][0]['usr']

def get_memory_usage():
    output = run(["vmstat", "-s"], capture_output=True, text=True).stdout.splitlines()
    total = output[0].rstrip().split(' ')[6]
    used = output[1].rstrip().split(' ')[6]
    print(total, used)
    return (int(used) / int(total)) * 100

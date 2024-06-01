from shutil import which
from sys import exit

KNOWN_DEPENDENCIES = [
    "uname",
    "uptime",
    "mpstat",
    "vmstat"
]

def check_dependencies():
    missing = []
    for dep in KNOWN_DEPENDENCIES:
        if which(dep) is None:
            missing.append(dep)

    if missing:
        print(f"The following dependencies are missing: {', '.join(missing)}. Please install them!")
        exit(1)



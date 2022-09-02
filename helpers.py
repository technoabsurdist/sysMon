from processes import sorted_processes
import psutil

# Helper functions for CPU and RAM usage
def cpu_usage() -> list:
    '''CPU usage per CPU'''
    return psutil.cpu_percent(4, percpu=True)

def ram_usage() -> float:
    '''RAM usage'''
    return psutil.virtual_memory()[2]

def processes_by_cpu(sort_by) -> list:
    '''List of running processes sorted by CPU usage'''
    return sorted_processes(sort_by)

def processes_by_memory(sort_by) -> list:
    '''List of running processes sorted by memory usage'''    
    return sorted_processes(sort_by)
 
def separator():
    print("\n****************")

def average(lst):
    return sum(lst)/len(lst)

def wrapper_print(out):
    print(f"\n{bcolors.OKGREEN}{out}{bcolors.ENDC}\n")


# colors to print to terminal
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



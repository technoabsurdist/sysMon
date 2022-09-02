# Two imported functions to get list of processes by cpu and memory
from curses import wrapper
from processes import sorted_processes
from helpers import *
import time

CPU_USAGE_KEY = 'cpu_percent'
MEM_USAGE_KEY = 'memory_percent'

formatted_usage_list = lambda x: str(x) + "%\n"

def main():
    proc_cpu = processes_by_cpu(CPU_USAGE_KEY)
    proc_mem = processes_by_memory(MEM_USAGE_KEY)
    intro()
    cpu_info()
    ram_info()

    # Top 10 Process by CPU and RAM
    wrapper_print("Top Processes by CPU utilization")
    formatter(proc_cpu[:10])
    wrapper_print("Top Processes by RAM utilization") 
    formatter(proc_mem[:10])

def formatter(processes):
    names = []
    memory_uses = []
    # iterate through list of objects
    for process in processes:
        # iterate through key value par in each object
        for key, value in process.items():
            if key == "name":
                names.append(value)
            if key == "memory_percent":
                memory_uses.append(value)
    names_to_memory = list(zip(names, memory_uses))
    for i in range(len(names_to_memory)):
        print(f"{names_to_memory[i][0]} -> {names_to_memory[i][1]}%")

def intro():
    '''Prints introduction to SyMonit'''
    # Printing
    print("\nThanks for using SyMonit. Processing your system monitor review.")
    time.sleep(0.5)
    print(f"\n{bcolors.UNDERLINE}Processing your results...{bcolors.ENDC}")
    
def cpu_info():
    '''Print all --formatted-- CPU info'''
    # CPU
    cpu_usage_list = cpu_usage()
    wrapper_print(f"CPU Usage per your {len(cpu_usage_list)} CPU(s)")
    formatted_list = [str(x) + "%, " for x in cpu_usage_list]
    for item in formatted_list:
        print(item, end="")
    print("\n\nAverage use per CPU --> ", average(cpu_usage_list))
    print("\nMax used CPU --> ", max(cpu_usage_list))

def ram_info():
    '''Print all --formatted-- RAM info'''
    # RAM
    ram_usage_list = ram_usage()
    wrapper_print("RAM Total Usage")
    print(str(ram_usage_list) + "%")

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











# run main
main()


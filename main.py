# Two imported functions to get list of processes by cpu and memory
from processes import sorted_processes
from helpers import *

CPU_USAGE_KEY = 'cpu_percent'
MEM_USAGE_KEY = 'memory_percent'

def main():
    cpu_usage_list = cpu_usage()
    ram_usage_list = ram_usage()
    proc_cpu = processes_by_cpu(CPU_USAGE_KEY)
    proc_mem = processes_by_memory(MEM_USAGE_KEY)
    # Printing
    separator()
    print("\nCPU Usage per CPU --> ", cpu_usage_list)
    separator()
    print("\nTotal RAM Usage --> ", ram_usage_list)
    separator()
    print("\nTop 10 Processes by CPU utilization --> ", proc_cpu[:10])
    separator()
    print("\nTop 10 Processes by RAM utilization --> ", proc_mem[:10])



main()


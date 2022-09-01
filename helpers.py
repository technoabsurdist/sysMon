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
    sorted_processes(sort_by)

def processes_by_memory(sort_by) -> list:
    '''List of running processes sorted by memory usage'''    
    return sorted_processes(sort_by)
 
def separator():
    print("\n****************")


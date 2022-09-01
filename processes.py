# Collection of functions to get current processes sorted by different metrics
from concurrent.futures import process
import psutil

def sorted_processes(sort_by) -> list:
    '''List of running processes sorted by `sort_by`'''
    list_proc = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(['pid', 'name', 'username', 'cpu_percent', 'memory_percent'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            list_proc.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    if (list_proc):
        sorted_list = sorted(list_proc, key=lambda i: i[sort_by], reverse=True) 
        return sorted_list  
    else:
        return []

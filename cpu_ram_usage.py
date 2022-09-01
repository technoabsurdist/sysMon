# Helper functions for CPU and RAM usage
def cpu_usage() -> list:
    '''CPU usage per CPU'''
    return psutil.cpu_percent(4, percpu=True)

def ram_usage() -> float:
    '''RAM usage'''
    return psutil.virtual_memory()[2]


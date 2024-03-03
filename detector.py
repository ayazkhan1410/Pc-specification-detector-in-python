import platform
import cpuinfo
import psutil
import GPUtil

def detect_specs():
    specs = {}
    
    # Get CPU information
    cpu_info = cpuinfo.get_cpu_info()
    specs['processor'] = cpu_info['brand_raw']
    
    # Get RAM information
    mem_info = psutil.virtual_memory()
    specs['ram'] = f"{mem_info.total / (1024 ** 3):.2f} GB"
    
    # Get GPU information
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu_info = gpus[0]
        specs['gpu'] = gpu_info.name
    else:
        specs['gpu'] = "No GPU detected"
    
    # Get storage information (assuming one disk)
    disk_info = psutil.disk_usage('/')
    specs['storage'] = f"{disk_info.total / (1024 ** 3):.2f} GB"

    return specs

if __name__ == "__main__":
    specs = detect_specs()
    for key, value in specs.items():
        print(f"{key.capitalize()}: {value}")
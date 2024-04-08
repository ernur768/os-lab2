# importing libraries
import platform
import psutil
import getpass
import socket
import time
import os


# function to get ip address
def get_ip_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception as e:
        return f"Error: {str(e)}"


# function to get system uptime
def get_system_uptime():
    try:
        return round(time.time() - psutil.boot_time())
    except Exception as e:
        return f"Error: {str(e)}"


# function to get cpu usage
def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return f"Error: {str(e)}"


# function to get running processes
def get_running_processes():
    try:
        processes = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'memory_percent'])
                processes.append(pinfo)
            except psutil.NoSuchProcess:
                pass
        return processes
    except Exception as e:
        return f"Error: {str(e)}"


# function to get disk partitions
def get_disk_partitions():
    try:
        partitions = psutil.disk_partitions()
        return [{'Device': partition.device, 'Mount Point': partition.mountpoint} for partition in partitions]
    except Exception as e:
        return f"Error: {str(e)}"


# function to get system architecture
def get_system_architecture():
    try:
        return platform.architecture()[0]
    except Exception as e:
        return f"Error: {str(e)}"


# function to get environment variables
def get_environment_variables():
    try:
        return dict(os.environ)
    except Exception as e:
        return f"Error: {str(e)}"


# function to combine all function to get information
def get_os_info():
    os_info = {
        'OS Name and Version': f"{platform.system()} {platform.release()}",
        'Processor Information': platform.processor(),
        'Memory (GB)': round(psutil.virtual_memory().total / (1024 ** 3), 2),
        'Available Disk Space (GB)': round(psutil.disk_usage('/').free / (1024 ** 3), 2),
        'Current User': getpass.getuser(),
        'IP Address': get_ip_address(),
        'System Uptime (seconds)': get_system_uptime(),
        'CPU Usage (%)': get_cpu_usage(),
        'Running Processes': get_running_processes(),
        'Disk Partitions': get_disk_partitions(),
        'System Architecture': get_system_architecture(),
        'Environment Variables': get_environment_variables()
    }
    return os_info


# function to print header
def print_header(header):
    print("=" * 50)
    print(header.center(50))
    print("=" * 50)
    print()


# main function is entry point that runs other functions
def main():
    print_header("System Information")
    os_info = get_os_info()
    for key, value in os_info.items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  {item}")
        else:
            print(f"{key}: {value}")

    input()


if __name__ == "__main__":
    main()

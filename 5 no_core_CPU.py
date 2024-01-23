import os
import multiprocessing

def get_cpu_info():
    try:
        # Get the number of CPU cores
        num_cores = os.cpu_count()

        # Get the number of CPU threads
        num_threads = multiprocessing.cpu_count()

        return num_cores, num_threads
    except Exception as e:
        return None, None

if __name__ == "__main__":
    cores, threads = get_cpu_info()

    if cores is not None and threads is not None:
        print(f"Number of CPU Cores: {cores}")
        print(f"Number of CPU Threads: {threads}")
    else:
        print("Unable to determine CPU information.")

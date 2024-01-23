import psutil

def get_ram_size():
    try:
        # Get system memory information
        mem_info = psutil.virtual_memory()

        # Extract the total RAM size in gigabytes
        ram_size_gb = mem_info.total / (1024 ** 3)

        return ram_size_gb

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    ram_size = get_ram_size()
    print(f"RAM Size: {ram_size:.2f} GB")

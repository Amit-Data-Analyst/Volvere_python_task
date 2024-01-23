import platform
import os

def get_cpu_model():
    if platform.system() == 'Windows':
        return platform.processor()
    elif platform.system() == 'Linux':
        try:
            # Read the /proc/cpuinfo file on Linux to get CPU information
            with open('/proc/cpuinfo', 'r') as file:
                for line in file:
                    if line.startswith('model name'):
                        return line.split(':')[1].strip()
        except FileNotFoundError:
            pass
    elif platform.system() == 'Darwin':
        # Use sysctl command on macOS to get CPU information
        return os.popen('sysctl -n machdep.cpu.brand_string').read().strip()

    # Return a default message if the platform is not recognized
    return "Unable to determine CPU model on this platform."

if __name__ == "__main__":
    cpu_model = get_cpu_model()
    print(f"CPU Model: {cpu_model}")

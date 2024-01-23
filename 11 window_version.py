import platform

def get_windows_version():
    try:
        # Get Windows version information
        windows_version = platform.version()

        return windows_version

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    windows_version = get_windows_version()

    if windows_version:
        print(f"Windows Version: {windows_version}")
    else:
        print("Unable to determine Windows version.")

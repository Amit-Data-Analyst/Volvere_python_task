import winreg

def get_installed_software():
    software_list = []

    try:
        # Open the registry key for installed software
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

        # Iterate through subkeys to get information about installed software
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)

            try:
                # Try to get the DisplayName value (name of the software)
                display_name, _ = winreg.QueryValueEx(subkey, 'DisplayName')
                software_list.append(display_name)
            except FileNotFoundError:
                pass  # Some subkeys may not have DisplayName value

            subkey.Close()

    except Exception as e:
        print(f"An error occurred: {e}")

    return software_list

if __name__ == "__main__":
    installed_software = get_installed_software()

    if installed_software:
        print("Installed Software:")
        for software in installed_software:
            print(software)

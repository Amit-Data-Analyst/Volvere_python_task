# Import the Speedtest class from the speedtest module
import speedtest

# Define a function named check_speed
def check_speed():
    # Create an instance of the Speedtest class
    st = speedtest.Speedtest()

    # Print a message indicating that the download speed is being checked
    print("Checking download speed...")

    # Call the download method of the Speedtest instance to measure the download speed
    download_speed = st.download()

    # Print the download speed in megabits per second (Mbps)
    print(f"Download Speed: {download_speed / 1_000_000:.2f} Mbps")

    # Print a newline for better formatting
    print("\nChecking upload speed...")

    # Call the upload method of the Speedtest instance to measure the upload speed
    upload_speed = st.upload()

    # Print the upload speed in megabits per second (Mbps)
    print(f"Upload Speed: {upload_speed / 1_000_000:.2f} Mbps")

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the check_speed function to check and print the internet speed
    check_speed()

import requests

def get_public_ip():
    try:
        # Make a request to a service that echoes your public IP address
        response = requests.get("https://httpbin.org/ip")

        # Parse the JSON response to get the public IP address
        public_ip = response.json().get("origin")

        return public_ip

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    public_ip = get_public_ip()

    if public_ip:
        print(f"Public IP Address: {public_ip}")
    else:
        print("Unable to determine public IP address.")

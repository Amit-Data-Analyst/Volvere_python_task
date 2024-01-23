import GPUtil

def get_gpu_model():
    try:
        # Get a list of GPU devices
        gpus = GPUtil.getGPUs()

        if gpus:
            # Get the model of the first GPU
            return gpus[0].name
        else:
            return "No GPU found."

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    gpu_model = get_gpu_model()
    print(f"GPU Model: {gpu_model}")

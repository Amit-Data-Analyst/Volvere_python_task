import tkinter as tk

def get_screen_resolution():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

if __name__ == "__main__":
    resolution = get_screen_resolution()
    print(f"Screen Resolution: {resolution[0]}x{resolution[1]} pixels")

import tkinter as tk
import math

def get_screen_size():
    try:
        root = tk.Tk()

        # Get the screen width and height in pixels
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Get the screen DPI
        screen_dpi = root.winfo_fpixels('1i')

        # Calculate the diagonal size in inches using the Pythagorean theorem
        diagonal_size = math.sqrt(screen_width**2 + screen_height**2) / screen_dpi

        root.destroy()

        return diagonal_size

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    screen_size = get_screen_size()

    if isinstance(screen_size, float):
        print(f"Screen Size: {screen_size:.2f} inches")
    else:
        print(screen_size)

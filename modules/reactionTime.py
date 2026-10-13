import sys
from pynput import mouse


def clear_screen():
    print("\033[2J\033[H", end="")


def print_header():
    print(
      "\n  -----------------------\n"
        "    Reaction Time Cheat  \n"
        "       By TheDirtMan     \n"
        "  -----------------------\n"
    )


def select_pixel(prompt):
    print(f"  {prompt}")
    position = None

    def on_click(x, y, button, pressed):
        nonlocal position

        if pressed:
            position = (x, y)
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return position


def get_delay(prompt=""):
    value = input(prompt).strip()

    if not value:
        return 0

    try:
        value = int(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print("\nERROR: Delay values must be non-negative integers.\n")
        sys.exit(1)

    return value


# Configuration
clear_screen()
print_header()

print("  Options (leave blank for default):\n")
print("  Artificial Delay (0ms): ")
print("  Random Delay Offset (0ms): ")

print("\033[2A", end="")
print("\033[26C", end="", flush=True)

delay = get_delay()
delayOffset = get_delay("\r\033[29C")


# Pixel selection
clear_screen()
print_header()

readPixel = select_pixel("Click the pixel to read color from...")
clickPixel = select_pixel("\n  Click the pixel to output to...")


# Main program
clear_screen()
print_header()
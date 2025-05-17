"""
Mouse Position Tracker Utility
-----------------------------
A development utility for tracking and displaying the current mouse
position coordinates in real-time. Used for determining UI element
locations for the reservation bot script.
"""

import sys
import time

import pyautogui


def track_mouse_position(refresh_rate=0.1):
    """
    Continuously track and display the current mouse cursor position.

    Args:
        refresh_rate (float): How often to update the position (in seconds)
                             Lower values provide more updates but consume more CPU

    Returns:
        int: 0 on successful termination, 1 on error
    """
    print("Press Ctrl-C to exit")
    try:
        while True:
            # Get current cursor position
            x, y = pyautogui.position()

            # Get RGB color at cursor position
            r, g, b = pyautogui.pixel(x, y)
            output = f'"position": ({x:4d},{y:4d}), "color": ({r:3d},{g:3d},{b:3d}),'

            # Update display in-place without line break
            print(f"\r{output}", end="", flush=True)

            # Wait before next update
            time.sleep(refresh_rate)
    except KeyboardInterrupt:
        # Handle normal exit via Ctrl-C
        print("\nMouse tracking stopped.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"\nAn error occurred: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(track_mouse_position())

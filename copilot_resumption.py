"""
Copilot Resumption Automation Tool
----------------------------------
This script monitors a specific screen region for color changes and
automatically inputs text when the target color is detected. It's designed
to help resume or continue Copilot sessions by automatically detecting
when interaction is needed and providing the appropriate response.
"""

import logging
import time

import numpy as np
import pyautogui

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("copilot_resumption.log"), logging.StreamHandler()],
)

# Configuration constants
DEFAULT_TOLERANCE = 10  # Default color tolerance value
DEFAULT_MONITOR_INTERVAL = 0.1  # Default monitoring interval in seconds
DEFAULT_INPUT_TEXT = "continue"  # Default text to input when color is detected
FOCUS_WAIT_TIME = 0.2  # Time to wait for text box to gain focus
TRIGGER_COOLDOWN = 1.0  # Cooldown time to avoid repeated triggers


def monitor_color_in_region(
    left, top, right, bottom, target_color, text_box_x, text_box_y, tolerance=10
):
    """
    Monitor a rectangular screen region for color changes and trigger text input.

    Args:
        left (int): Left coordinate of the monitoring region
        top (int): Top coordinate of the monitoring region
        right (int): Right coordinate of the monitoring region
        bottom (int): Bottom coordinate of the monitoring region
        target_color (tuple): Target RGB color values (R, G, B)        text_box_x (int): X coordinate of the text input box
        text_box_y (int): Y coordinate of the text input box
        tolerance (int): Color tolerance value for matching
    """
    # Calculate region dimensions
    width = right - left
    height = bottom - top

    logging.info(
        f"Starting color monitoring for region: ({left}, {top}) to ({right}, {bottom})"
    )
    logging.info(f"Target color: RGB{target_color}")
    logging.info(f"Text box position: ({text_box_x}, {text_box_y})")

    while True:
        try:
            # Capture screenshot of the specified region
            screenshot = pyautogui.screenshot(region=(left, top, width, height))

            # Convert to numpy array for processing
            img_array = np.array(screenshot)

            # Check if target color exists in the region
            if color_exists_in_image(img_array, target_color, tolerance):
                logging.info(
                    "Target color detected! Executing input operation..."
                )  # Click on text box position
                pyautogui.click(text_box_x, text_box_y)
                time.sleep(FOCUS_WAIT_TIME)  # Wait for text box to gain focus

                # Input the specified text
                pyautogui.write(DEFAULT_INPUT_TEXT)

                # Press Enter key
                pyautogui.press("enter")

                logging.info(
                    f"Successfully input '{DEFAULT_INPUT_TEXT}' and pressed Enter"
                )

                # Optional: break if only one execution is needed
                # break  # Uncomment this line if you only want to execute once

                time.sleep(TRIGGER_COOLDOWN)  # Avoid repeated triggers

        except Exception as e:
            logging.error(f"Error occurred during monitoring: {str(e)}")

        # Monitoring interval
        time.sleep(DEFAULT_MONITOR_INTERVAL)


def color_exists_in_image(img_array, target_color, tolerance):
    """
    Check if a specified color exists within an image array.

    Args:
        img_array (numpy.ndarray): Image array in RGB format
        target_color (tuple): Target RGB color values (R, G, B)
        tolerance (int): Color tolerance for matching

    Returns:
        bool: True if the target color exists within tolerance, False otherwise
    """
    target_r, target_g, target_b = target_color

    # Calculate color difference for each pixel
    r_diff = np.abs(img_array[:, :, 0] - target_r)
    g_diff = np.abs(img_array[:, :, 1] - target_g)
    b_diff = np.abs(img_array[:, :, 2] - target_b)

    # Check if any pixels are within tolerance range
    color_match = (r_diff <= tolerance) & (g_diff <= tolerance) & (b_diff <= tolerance)

    return np.any(color_match)


# Configuration for the monitoring region and target
MONITOR_REGION = {
    "left": 1180,  # Left boundary of monitoring region
    "top": 420,  # Top boundary of monitoring region
    "right": 1919,  # Right boundary of monitoring region
    "bottom": 840,  # Bottom boundary of monitoring region
}

TARGET_COLOR = (0, 120, 212)  # Target RGB color (blue)
TEXT_BOX_POSITION = (1296, 917)  # Text input box coordinates
COLOR_TOLERANCE = 15  # Color matching tolerance


def main():
    """
    Main execution function that starts the Copilot resumption process.
    Configures the monitoring parameters and begins the detection loop.
    """
    try:
        logging.info("Starting Copilot resumption automation tool")

        # Start monitoring with configured parameters
        monitor_color_in_region(
            MONITOR_REGION["left"],
            MONITOR_REGION["top"],
            MONITOR_REGION["right"],
            MONITOR_REGION["bottom"],
            TARGET_COLOR,
            TEXT_BOX_POSITION[0],
            TEXT_BOX_POSITION[1],
            tolerance=COLOR_TOLERANCE,
        )

    except KeyboardInterrupt:
        logging.info("Copilot resumption monitoring stopped by user")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()

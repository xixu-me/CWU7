"""
Badminton Court Reservation Bot
-------------------------------
This script automates the process of reserving a badminton court at
precisely the configured time. It navigates through the reservation
interface, handles CAPTCHA challenges, and logs the entire process.
"""

import logging
import time
from datetime import datetime, timedelta

import ddddocr
import numpy as np
import pyautogui
from PIL import Image

# Configure logging to both file and console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("reservation.log"), logging.StreamHandler()],
)

# Configuration constants
RESERVATION_HOUR = 7  # Target hour for reservation (24-hour format)
RESERVATION_MINUTE = 0  # Target minute for reservation
COORDINATES = {
    "miniprogram_icon": (1093, 225),  # Position of the mini-program icon
    "title_bar": (973, 21),  # Title bar position
    "right_edge": (1919, 150),  # Screen right edge position
    "reservation_button": (1557, 546),  # Reservation button position
    "venue_button": (1260, 332),  # Main venue category selection
    "badminton_button": (1101, 223),  # Main badminton category selection
    "reserve_button": (1017, 355),  # Reserve action button
    "court_selection": (1401, 516),  # Specific court selection
    "confirm_button": (1439, 991),  # Final confirmation button
    "captcha_input": (1851, 570),  # CAPTCHA input field
    "captcha_region": (1628, 550, 1776, 592),  # Screen region containing CAPTCHA image
    "close_button": (1886, 27),  # Close button for the miniprogram window
}

# Pixel check points and expected colors for each UI stage
PIXEL_CHECKS = {
    "miniprogram_loaded": {
        "position": (1505, 229),
        "color": (54, 61, 77),
        "timeout": 1,
    },
    "reservation_page_loaded": {
        "position": (1019, 351),
        "color": (255, 161, 18),
        "timeout": 1,
    },
    "venue_page_loaded": {
        "position": (1038, 133),
        "color": (255, 161, 18),
        "timeout": 1,
    },
    "court_page_loaded": {
        "position": (1192, 988),
        "color": (149, 152, 159),
        "timeout": 1,
    },
    "court_selected": {"position": (1138, 993), "color": (46, 49, 66), "timeout": 1},
}

CAPTCHA_CHECK_PIXEL = (1109, 987)  # Pixel to check for CAPTCHA presence
CAPTCHA_CHECK_COLOR = (46, 49, 66)  # Expected color when CAPTCHA is visible
MAX_RETRY_ATTEMPTS = 100  # Maximum retry attempts


def wait_until_scheduled_time():
    """
    Suspends execution until the configured reservation time approaches.
    Sleeps until 10 seconds before the target time, then actively polls
    to ensure precise timing.
    """
    logging.info(
        f"Waiting until {RESERVATION_HOUR}:{RESERVATION_MINUTE:02d} to start reservation process"
    )
    target_time = datetime.now().replace(
        hour=RESERVATION_HOUR, minute=RESERVATION_MINUTE, second=0, microsecond=0
    )
    if target_time < datetime.now():
        target_time += timedelta(days=1)
    time_to_sleep = (target_time - datetime.now()).total_seconds() - 10
    if time_to_sleep > 0:
        logging.info(f"Sleeping for {time_to_sleep:.2f} seconds")
        time.sleep(time_to_sleep)
    while datetime.now() < target_time:
        time.sleep(0.01)
    logging.info("Starting reservation process")


def wait_for_pixel_color(position, color, timeout=1, check_interval=0.01):
    """
    Wait until the pixel at the given position changes to the expected color or timeout is reached.

    Args:
        position (tuple): (x, y) coordinates of the pixel to check
        color (tuple): Expected RGB color value (r, g, b)
        timeout (float): Maximum time to wait in seconds
        check_interval (float): Time between checks in seconds

    Returns:
        bool: True if the pixel color matched, False if timeout was reached
    """
    x, y = position
    start_time = time.time()
    logging.info(f"Waiting for pixel at ({x}, {y}) to change to color {color}")

    while time.time() - start_time < timeout:
        pixel_color = Image.fromarray(
            np.array(pyautogui.screenshot(region=(x, y, 1, 1)))
        ).getpixel((0, 0))

        # Check if colors are close enough (allow small variations)
        if pixel_color == color:
            logging.info(f"Pixel color matched: {pixel_color}")
            return True

        time.sleep(check_interval)

    logging.warning(
        f"Timeout waiting for pixel at ({x}, {y}) to change to {color}, current color: {pixel_color}"
    )
    return False


def click_at(position_name):
    """
    Click at a predefined position on the screen.

    Args:
        position_name (str): Key name from COORDINATES dictionary
    """
    x, y = COORDINATES[position_name]
    logging.info(f"Clicking {position_name} at ({x}, {y})")
    pyautogui.click(x, y)


def hold_and_drag(start_position_name, end_position_name):
    """
    Hold the mouse button down at the start position and drag to the end position.

    Args:
        start_position_name (str): Key name from COORDINATES for the start position
        end_position_name (str): Key name from COORDINATES for the end position
    """
    start_x, start_y = COORDINATES[start_position_name]
    end_x, end_y = COORDINATES[end_position_name]
    logging.info(
        f"Holding mouse at {start_position_name} ({start_x}, {start_y}) and dragging to {end_position_name} ({end_x}, {end_y})"
    )
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=0.2)  # duration for a smoother drag
    pyautogui.mouseUp()


def solve_captcha():
    """
    Capture, process and recognize the CAPTCHA text.

    Returns:
        str: Recognized text from the CAPTCHA image
    """
    left, top, right, bottom = COORDINATES["captcha_region"]
    screenshot = pyautogui.screenshot()
    captcha_img = screenshot.crop((left, top, right, bottom))
    captcha_img.save("captcha.png")  # Save for debugging/analysis purposes

    # Initialize OCR engine and recognize CAPTCHA
    ocr = ddddocr.DdddOcr(show_ad=False)
    with open("captcha.png", "rb") as f:
        img_bytes = f.read()
    captcha_text = ocr.classification(img_bytes)
    logging.info(f"CAPTCHA recognized as: {captcha_text}")
    return captcha_text


def input_captcha(text):
    """
    Input the recognized CAPTCHA text into the appropriate field.

    Args:
        text (str): CAPTCHA text to input
    """
    click_at("captcha_input")
    # Wait briefly for input focus
    time.sleep(0.01)
    pyautogui.hotkey("ctrl", "a")  # Select all existing text
    pyautogui.typewrite(text)


def is_captcha_showing():
    """
    Check if the CAPTCHA challenge is currently displayed.

    Returns:
        bool: True if CAPTCHA is displayed, False otherwise
    """
    x, y = CAPTCHA_CHECK_PIXEL
    pixel_color = Image.fromarray(
        np.array(pyautogui.screenshot(region=(x, y, 1, 1)))
    ).getpixel((0, 0))
    return pixel_color == CAPTCHA_CHECK_COLOR


def close_window_and_restart():
    """
    Close the current mini-program window and wait a short period
    """
    logging.info("Closing the mini-program window and preparing to restart")
    click_at("close_button")


def reservation_process():
    """
    Execute the complete reservation process
    """
    # Click on the mini-program icon to open the reservation interface
    click_at("miniprogram_icon")

    # Move window to the edge
    hold_and_drag("title_bar", "right_edge")
    if not wait_for_pixel_color(**PIXEL_CHECKS["miniprogram_loaded"]):
        return False

    # Navigate through reservation interface
    click_at("reservation_button")
    if not wait_for_pixel_color(**PIXEL_CHECKS["reservation_page_loaded"]):
        return False

    click_at("venue_button")
    if not wait_for_pixel_color(**PIXEL_CHECKS["venue_page_loaded"]):
        return False

    click_at("badminton_button")
    click_at("reserve_button")
    if not wait_for_pixel_color(**PIXEL_CHECKS["court_page_loaded"]):
        return False

    click_at("court_selection")
    if not wait_for_pixel_color(**PIXEL_CHECKS["court_selected"]):
        return False

    click_at("confirm_button")

    # Handle CAPTCHA if presented
    captcha_attempts = 0
    while is_captcha_showing() and captcha_attempts < 10:
        captcha_attempts += 1
        logging.info(f"CAPTCHA attempt {captcha_attempts}")
        captcha_text = solve_captcha()
        input_captcha(captcha_text)
        time.sleep(0.05)
        click_at("confirm_button")
        time.sleep(0.2)

    if captcha_attempts >= 10:
        logging.warning(
            "CAPTCHA recognition failed more than 10 times, need to restart"
        )
        return False
    else:
        logging.info("Reservation process completed")
        return True


def main():
    """
    Main execution function that orchestrates the reservation process.
    Handles the sequence of UI interactions and CAPTCHA solving.
    """
    try:
        pyautogui.FAILSAFE = False  # Disable failsafe to prevent interruptions
        wait_until_scheduled_time()

        retry_count = 0
        success = False

        while not success and retry_count < MAX_RETRY_ATTEMPTS:
            try:
                if retry_count > 0:
                    logging.info(f"Retry reservation attempt {retry_count}")
                success = reservation_process()

                if not success:
                    retry_count += 1
                    close_window_and_restart()
            except Exception as e:
                logging.error(f"Error occurred during reservation process: {str(e)}")
                retry_count += 1
                close_window_and_restart()

        if success:
            logging.info("Reservation successfully completed!")
        else:
            logging.error(
                f"Failed to complete reservation after {MAX_RETRY_ATTEMPTS} attempts"
            )

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()

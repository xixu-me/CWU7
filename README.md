# CWU7 - Can't Wake Up at 7am

A Python automation tool for reserving badminton courts right when they become available at 7:00 AM.

## Overview

CWU7 automates the process of reserving badminton courts at exactly the configured time. If you hate waking up early to book courts when they first become available, this bot can help by:

- Automatically navigating through the reservation website
- Handling CAPTCHA challenges using OCR
- Precisely timing the reservation attempt
- Logging the entire process

## Features

- **Precise Timing**: Automatically executes at exactly 7:00 AM (or your configured time)
- **CAPTCHA Solving**: Uses OCR technology to automatically solve CAPTCHA challenges
- **Position Tracking**: Includes a utility for determining UI element coordinates
- **Detailed Logging**: Records the entire reservation process for troubleshooting

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xixu-me/CWU7.git
   cd CWU7
   ```

2. Install dependencies:

   ```bash
   pip install pyautogui pillow numpy ddddocr
   ```

## Usage

### Mouse Position Tracker

Before using the reservation bot, you need to determine the screen coordinates for various UI elements:

```bash
python tracker.py
```

Move your cursor to important UI elements and note their coordinates. Then update these in the run.py file.

### Reservation Bot

To run the reservation bot:

```bash
python run.py
```

By default, the bot will wait until 7:00 AM to begin the reservation process.

## Configuration

Edit the following constants in run.py to customize the bot:

- `RESERVATION_HOUR` and `RESERVATION_MINUTE`: Set the target time for reservation
- `COORDINATES`: Adjust the screen coordinates for various UI elements
- `WAIT_TIMES`: Modify the timing between actions if needed

```python
# Example configuration
RESERVATION_HOUR = 7  # Target hour (24-hour format)
RESERVATION_MINUTE = 0  # Target minute
COORDINATES = {
    "badminton_button": (1101, 223),
    # ...other coordinates
}
```

## How It Works

1. The script waits until the configured time (default 7:00 AM)
2. It performs a sequence of clicks to navigate the reservation interface
3. If a CAPTCHA appears, it:
   - Captures the CAPTCHA image from the screen
   - Uses OCR to recognize the text
   - Inputs the recognized text
   - Submits the form
4. The process is logged to both console and file (`reservation.log`)

## Troubleshooting

- If the bot fails to click on the right locations, use tracker.py to verify and update coordinates
- Check `reservation.log` for detailed error information
- Make sure your screen resolution matches the one used for configuring coordinates

## Disclaimer

This tool is for educational purposes only. Using automated bots might be against the terms of service of some reservation systems. Use at your own risk.

## License

Licensed under the [GPL-3.0](LICENSE) license.  

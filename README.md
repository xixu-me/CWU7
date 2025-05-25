# CWU7 - Can't Wake Up at 7am

A Python automation script for reserving badminton courts at precisely 7:00 AM. This bot navigates through the reservation interface, handles CAPTCHA challenges, and logs the entire process.

## Features

- **Precise Timing**: Waits until exactly 7:00 AM to start the reservation process
- **Automated Navigation**: Clicks through the reservation interface automatically
- **CAPTCHA Solving**: Uses OCR to recognize and solve CAPTCHA challenges
- **Retry Logic**: Automatically retries on failure with configurable attempts
- **Comprehensive Logging**: Logs all actions and errors to file and console
- **Mouse Tracking Utility**: Includes a helper tool for finding UI coordinates

## Requirements

- Python 3.6+
- Windows operating system
- Required Python packages:

  ```
  pyautogui
  ddddocr
  numpy
  Pillow
  ```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/xixu-me/CWU7.git
   cd CWU7
   ```

2. Install required dependencies:

   ```bash
   pip install pyautogui ddddocr numpy Pillow
   ```

## Usage

### Running the Reservation Bot

1. Configure the reservation time and coordinates in `run.py` if needed
2. Run the main script:

   ```bash
   python run.py
   ```

The bot will wait until 7:00 AM and then automatically attempt to reserve a badminton court.

### Mouse Position Tracker

Use the tracker utility to find coordinates for UI elements:

```bash
python tracker.py
```

This will display the current mouse position and pixel color in real-time. Press Ctrl+C to exit.

## Configuration

### Time Settings

Modify these constants in `run.py` to change the reservation time:

```python
RESERVATION_HOUR = 7    # Target hour (24-hour format)
RESERVATION_MINUTE = 0  # Target minute
```

### Coordinates

The `COORDINATES` dictionary in `run.py` contains all click positions. Use `tracker.py` to find the correct coordinates for your screen resolution and interface.

### Retry Settings

```python
MAX_RETRY_ATTEMPTS = 100  # Maximum retry attempts
```

## How It Works

1. **Wait for Target Time**: The script waits until the configured reservation time
2. **Open Mini-Program**: Clicks on the reservation interface
3. **Navigate Interface**: Automatically clicks through the reservation steps
4. **Handle CAPTCHA**: Uses OCR to solve any CAPTCHA challenges
5. **Retry on Failure**: Automatically retries if any step fails
6. **Log Results**: Records all actions and results

## File Structure

- `run.py` - Main reservation bot script
- `tracker.py` - Mouse position tracking utility
- `LICENSE` - GNU GPL v3 license
- `.gitignore` - Git ignore file
- `reservation.log` - Generated log file (created during execution)

## Troubleshooting

### Common Issues

1. **Wrong Coordinates**: Use `tracker.py` to find the correct click positions
2. **CAPTCHA Failures**: The OCR may need adjustment for different CAPTCHA styles
3. **Timing Issues**: Adjust the `check_interval` in pixel checking functions
4. **Screen Resolution**: Coordinates may need adjustment for different screen sizes

### Logs

Check `reservation.log` for detailed execution logs and error messages.

## Legal Notice

This software is provided for educational purposes only. Users are responsible for compliance with the terms of service of the reservation system. The authors are not responsible for any misuse or violations.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Disclaimer

This is an automation tool designed to help with legitimate reservations. Please use responsibly and in accordance with the reservation system's terms of service.

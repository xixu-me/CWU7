# CWU7 - Can't Wake Up at 7am

A Python automation toolkit for badminton court reservations and development assistance. The main script automates court reservations at precisely 7:00 AM, while additional utilities help with UI coordination and Copilot session management.

## 🚀 Features

### Core Reservation Bot

- **⏰ Precise Timing**: Waits until exactly 7:00 AM to start the reservation process
- **🤖 Automated Navigation**: Clicks through the reservation interface automatically
- **🔍 CAPTCHA Solving**: Uses OCR technology to recognize and solve CAPTCHA challenges
- **🔄 Retry Logic**: Automatically retries on failure with configurable attempts
- **📝 Logging**: Logs all actions and errors to file and console

### Utilities

- **🎯 Mouse Tracking**: Helper tool for finding UI coordinates
- **💬 Copilot Resumption**: Tool to resume Copilot sessions by monitoring screen color and automating input

## 📋 Requirements

- Python 3.6+
- Windows OS
- Python packages:
  - pyautogui
  - ddddocr
  - numpy
  - Pillow

## 🛠️ Installation

```powershell
# Clone the repository
git clone https://github.com/xixu-me/CWU7.git
cd CWU7

# Install dependencies
pip install pyautogui ddddocr numpy Pillow
```

## 📖 Usage

### Reservation Bot

1. Edit `court_reservation.py` to set reservation time and coordinates if needed.
2. Run:

   ```powershell
   python court_reservation.py
   ```

### Mouse Position Tracker

Find UI coordinates:

```powershell
python tracker.py
```

Shows mouse position and pixel color in real-time. Press Ctrl+C to exit.

### Copilot Resumption Tool

Resume Copilot sessions automatically:

```powershell
python copilot_resumption.py
```

Monitors a screen region for color changes and inputs text to help resume Copilot sessions when interaction is needed.

## ⚙️ Configuration

- **Time**: Edit `RESERVATION_HOUR` and `RESERVATION_MINUTE` in `court_reservation.py`.
- **Coordinates**: Update the `COORDINATES` dictionary in `court_reservation.py` using `tracker.py`.
- **Retry**: Set `MAX_RETRY_ATTEMPTS` in `court_reservation.py`.

## 🔧 How It Works

1. Waits for the target time
2. Opens the reservation interface
3. Navigates steps automatically
4. Handles CAPTCHA with OCR
5. Retries on failure
6. Logs all actions and results

## 📁 File Structure

- `court_reservation.py` - Main reservation bot
- `tracker.py` - Mouse position tracker
- `copilot_resumption.py` - Copilot session resumption tool
- `captcha.png` - Sample CAPTCHA image
- `LICENSE` - License
- `.gitignore` - Git ignore file
- `reservation.log` - Reservation log (created at runtime)
- `copilot_resumption.log` - Copilot tool log (created at runtime)

## 🔧 Troubleshooting

- **Wrong Coordinates**: Use `tracker.py` to find correct positions
- **CAPTCHA Failures**: OCR may need adjustment for different styles
- **Timing Issues**: Adjust `check_interval` in code
- **Screen Resolution**: Update coordinates for your display

Logs: See `reservation.log` and `copilot_resumption.log` for details.

## ⚖️ Legal Notice

This software is for educational purposes only. Users are responsible for compliance with the reservation system's terms. The authors are not responsible for misuse.

## 📄 License

GNU General Public License v3.0 - see [LICENSE](LICENSE).

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## ⚠️ Disclaimer

This tool is for legitimate reservations only. Use responsibly and follow the reservation system's terms of service.

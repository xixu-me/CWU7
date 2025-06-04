# CWU7 - Can't Wake Up at 7am

A modular Python automation toolkit featuring multiple independent tools for various automation and development tasks. The toolkit is designed with equal-status tools that can be used individually or together, with easy expansion capabilities for new automation tools.

## 🚀 Toolkit Overview

CWU7 consists of multiple standalone tools, each serving a specific automation purpose:

### 🏸 Court Reservation Tool ([`court_reservation.py`](tools/court_reservation.py))

An automated badminton court reservation system with intelligent timing and error handling:

- **⏰ Precise Timing**: Waits until exactly 7:00 AM to start the reservation process
- **🤖 Automated Navigation**: Clicks through the reservation interface automatically
- **🔍 CAPTCHA Solving**: Uses OCR technology to recognize and solve CAPTCHA challenges
- **🔄 Retry Logic**: Automatically retries on failure with configurable attempts
- **📝 Comprehensive Logging**: Logs all actions and errors to file and console

### 🎯 Mouse Position Tracker ([`mouse_tracker.py`](tools/mouse_tracker.py))

A development utility for UI automation coordinate discovery:

- **📍 Real-time Coordinates**: Displays live mouse position and pixel color information
- **🖱️ Developer-Friendly**: Essential for determining click coordinates for automation scripts
- **⚡ Low Latency**: Configurable refresh rate for optimal performance
- **🎨 Color Detection**: Shows RGB values for precise color-based automation

### 💬 Copilot Resumption Tool ([`copilot_resumption.py`](tools/copilot_resumption.py))

An intelligent session management tool for automated development assistance:

- **👁️ Screen Monitoring**: Watches specific screen regions for color changes
- **🤖 Auto-Response**: Automatically inputs text when interaction is needed
- **🔄 Session Continuity**: Helps maintain active Copilot sessions without manual intervention
- **📊 Activity Logging**: Tracks all monitoring and response activities

## 📋 Requirements

- Python 3.6+
- Windows OS
- Python packages:
  - pyautogui
  - ddddocr
  - numpy
  - Pillow

## 🛠️ Installation

```shell
# Clone the repository
git clone https://github.com/xixu-me/CWU7.git
cd CWU7

# Install dependencies
pip install pyautogui ddddocr numpy Pillow
```

## 📖 Tool Usage

Each tool in the CWU7 toolkit can be used independently. Choose the tool that fits your current automation needs:

### 🏸 Court Reservation Tool

Automate badminton court reservations at precise timing:

1. Configure reservation settings in `court_reservation.py` if needed
2. Run the tool:

   ```shell
   python tools/court_reservation.py
   ```

The tool will wait until the configured time and automatically handle the entire reservation process.

### 🎯 Mouse Position Tracker

Discover UI coordinates for automation scripts:

```shell
python tools/mouse_tracker.py
```

The tracker displays real-time mouse position and pixel color information. Press Ctrl+C to exit when you've found the coordinates you need.

### 💬 Copilot Resumption Tool

Automatically maintain active Copilot sessions:

```shell
python tools/copilot_resumption.py
```

The tool monitors screen regions and automatically responds to interaction prompts to keep Copilot sessions active.

## ⚙️ Tool Configuration

Each tool has its own configuration options. Refer to the specific tool's documentation within its source file:

### Court Reservation Tool

- **Timing**: Edit `RESERVATION_HOUR` and `RESERVATION_MINUTE` in `court_reservation.py`
- **UI Coordinates**: Update the `COORDINATES` dictionary using coordinates found with the tracker tool
- **Retry Settings**: Configure `MAX_RETRY_ATTEMPTS` for error handling

### Mouse Position Tracker

- **Refresh Rate**: Modify the `refresh_rate` parameter for update frequency
- **Display Format**: Customize output format in the tracker function

### Copilot Resumption Tool

- **Monitor Region**: Set the screen coordinates for color monitoring
- **Target Colors**: Configure the RGB values to detect interaction needs
- **Response Text**: Customize the automated input text

## 🔧 How It Works

The toolkit employs different automation strategies for each tool:

### Court Reservation Workflow

1. Waits for the target time
2. Opens the reservation interface
3. Navigates steps automatically
4. Handles CAPTCHA with OCR
5. Retries on failure
6. Logs all actions and results

### Mouse Tracker Operation

1. Captures mouse position continuously
2. Reads pixel color at cursor location
3. Displays formatted coordinate and color data
4. Updates at configurable intervals

### Copilot Resumption Process

1. Monitors specified screen region
2. Detects color changes indicating interaction needs
3. Automatically inputs configured response text
4. Logs all monitoring activities

## 🔧 Troubleshooting

### General Issues

- **Python Dependencies**: Ensure all required packages are installed via pip
- **Screen Resolution**: Update coordinates for your specific display configuration
- **Permission Issues**: Run with appropriate privileges if automation is blocked

### Tool-Specific Issues

#### Court Reservation Tool

- **Wrong Coordinates**: Use `mouse_tracker.py` to find correct UI element positions
- **CAPTCHA Failures**: OCR may need adjustment for different CAPTCHA styles
- **Timing Issues**: Adjust `check_interval` in the tool configuration

#### Mouse Position Tracker

- **High CPU Usage**: Increase refresh rate interval for lower resource consumption
- **Coordinate Accuracy**: Ensure display scaling is considered in measurements

#### Copilot Resumption Tool

- **Color Detection**: Verify RGB values match the actual screen colors
- **Response Timing**: Adjust monitoring intervals for better responsiveness

For detailed logs, check the respective log files: `reservation.log` and `copilot_resumption.log`.

## 🚀 Extending the Toolkit

CWU7 is designed for easy expansion. To add new automation tools:

### Adding New Tools

1. **Create Tool File**: Add your new tool to the `tools/` directory
2. **Follow Structure**: Use existing tools as templates for logging and configuration
3. **Update Documentation**: Add tool description to both README files
4. **Test Integration**: Ensure the tool works independently and with others

### Development Guidelines

- **Modular Design**: Each tool should be self-contained and independently executable
- **Consistent Logging**: Use the established logging format for consistency
- **Configuration**: Make settings easily configurable for different use cases
- **Error Handling**: Implement robust error handling and retry mechanisms

## ⚖️ Legal Notice

This software is for educational purposes only. Users are responsible for compliance with the terms of service of any systems they interact with. The authors are not responsible for misuse or any consequences of using this toolkit.

## 📄 License

GNU General Public License v3.0 - see [LICENSE](LICENSE).

## 🤝 Contributing

We welcome contributions to expand the CWU7 toolkit:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-tool`)
3. Commit your changes with clear messages
4. Push to your branch (`git push origin feature/new-tool`)
5. Create a Pull Request with detailed description

### Contribution Guidelines

- Follow the existing code style and structure
- Add comprehensive documentation for new tools
- Include error handling and logging
- Test thoroughly on Windows environments
- Update both English and Chinese README files

## ⚠️ Disclaimer

This toolkit is designed for legitimate automation purposes only. Users must:

- Respect terms of service of target systems
- Use tools responsibly and ethically
- Comply with applicable laws and regulations
- Take full responsibility for their usage

The authors assume no liability for misuse or any consequences arising from the use of this toolkit.

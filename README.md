# Python QR Code Generator

This repository contains a Python script that generates QR codes using the `segno` library. The QR code is created with the message "Hello, world!" and saved in both SVG and PNG formats. The script includes options to customize the QR code's size, border, and background.

## Requirements

- Python 3.x
- `segno` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/LahcenEzzara/python-qrcode-explorer.git

   cd python-qrcode-explorer
   ```

2. Install the required dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

## How to Use

The `main.py` script generates a QR code with the message "Hello, world!" and saves it in both SVG and PNG formats. You can customize the QR code's size, border, and background color. To run the script, use the following command:

```bash
python main.py
```

### Customizations
- **Border**: The QR code will have a border of 1 module unit.
- **Scale**: The QR code is scaled by a factor of 10.
- **Transparent Background**: The SVG file will have a transparent background.
- **Formats**: The QR code is saved in both SVG and PNG formats.

## Files

- `main.py`: Python script that generates the QR code.
- `qrcode.svg`: Generated QR code in SVG format with transparent background.
- `qrcode.png`: Generated QR code in PNG format.

## Example QR Code

After running the script, you'll get two files:
- `qrcode.svg`: The SVG version of the QR code with a transparent background.
- `qrcode.png`: The PNG version of the QR code with a border.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
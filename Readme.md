# Image Editor Application

## Overview
The Image Editor Application is a Python-based GUI tool designed for performing various image editing tasks. It provides an easy-to-use interface and supports a wide range of functionalities such as resizing, cropping, rotating, and compressing images.

## Features
- **Edit Image**:
  - Adjust brightness, contrast, sharpness, and color.
- **Compress Image**:
  - Compress by quality or DPI (resolution).
- **Resize Image**:
  - Resize to specific dimensions.
- **Crop Image**:
  - Crop by specifying coordinates.
- **Rotate Image**:
  - Rotate to a specified angle.
- **Blur Image**:
  - Apply Gaussian blur with adjustable radius.
- **Sharpen Image**:
  - Enhance image sharpness.
- **Edge Detection**:
  - Highlight edges for enhanced details.
- **Mirror Image**:
  - Create a mirrored version of an image.

## How to Use
1. Ensure the required dependencies are installed.
2. Place your images in the `Images` directory.
3. Run the `window.py` file to launch the application.
4. Use the intuitive GUI to edit images as desired.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ironsupr/Image_Editor
   ```
2. Install dependencies:
   ```bash
   pip install pillow customtkinter
   ```
3. Run the application:
   ```bash
   python window.py
   ```

## Directory Structure
- **`window.py`**: Main file for the GUI application.
- **`Image_Editor.py`**: Contains functions for image processing.
- **`Images`**: Directory for input images (update the path if needed).
- **Output Folders**: Automatically created for storing processed images.

## Dependencies
- Python 3.x
- Pillow
- customtkinter

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.


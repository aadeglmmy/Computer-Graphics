# Color Models Application

## Overview

This program is a graphical user interface (GUI) built using Python's Tkinter library, designed to demonstrate and convert between different color models: RGB, CMYK, and HLS (Hue, Lightness, Saturation). The user can adjust color values in one model, and the corresponding values in the other two models are automatically updated in real-time. Additionally, users can choose colors using a built-in color picker, and the selected color's values are reflected across all color models.

## Features

1. **RGB Color Model (Red, Green, Blue)**: 
   - Adjust RGB values using sliders or text entry fields.
   - Automatically updates the CMYK and HLS values based on the RGB inputs.

2. **CMYK Color Model (Cyan, Magenta, Yellow, Black)**:
   - Adjust CMYK values using sliders or text entry fields.
   - Automatically updates the RGB and HLS values based on the CMYK inputs.

3. **HLS Color Model (Hue, Lightness, Saturation)**:
   - Adjust HLS values using sliders or text entry fields.
   - Automatically updates the RGB and CMYK values based on the HLS inputs.

4. **Color Display**: 
   - A color box displays the currently selected color based on the model inputs.

5. **Color Picker**:
   - Users can choose a color from a color chooser dialog, and the chosen color will update all color model values (RGB, CMYK, and HLS) accordingly.

## Getting Started

### Prerequisites

To run the program, you need:
- Python 3.x installed on your system.
- The `tkinter` library (which is included by default in most Python distributions).

### Installation

1. Clone or download the repository to your local machine:
    ```bash
    git clone git@github.com:aadeglmmy/Computer-Graphics.git
    ```

2. Navigate to the directory where the script is saved:
    ```bash
    cd Computer-Graphics
    ```

3. Run the program:
    ```bash
    python KG1.py
    ```

### How to Use

1. **Adjusting Colors:**
   - You can change the values for any color model (RGB, CMYK, or HLS) using the sliders or by typing the values into the provided entry boxes.
   - The other color models will automatically adjust to reflect your changes.

2. **Choosing a Color:**
   - Press the "Choose color" button to open a color picker dialog.
   - Select a color, and its corresponding RGB, CMYK, and HLS values will be displayed in their respective sections.

3. **Real-time Color Preview:**
   - The `color_box` will show the currently selected color, giving you an instant visual preview as you adjust the color values.

### Customization

You can adjust the layout, size, or other visual aspects of the application by modifying the Tkinter components in the script. The current layout includes three primary sections (RGB, CMYK, and HLS), a color preview box, and a color picker button.

### Known Limitations

- The program assumes valid inputs within the defined range for each color model. However, input validation is implemented to clamp values to valid ranges.
- The CMYK to RGB conversion might not match exactly with what some design tools or color systems display, as different conversion algorithms may be used.

# Image Processing Application

This is a graphical application built with Python, `Tkinter`, `OpenCV`, and `PIL` libraries that allows users to load images and apply various filters for analysis and preprocessing. The program provides basic image processing tools, including thresholding, median filtering, and min/max filters.

## Features

- **Load Image**: Load a grayscale image for processing.
- **Otsu Thresholding**: Automatically calculates an optimal threshold to separate objects in an image.
- **Fixed Thresholding**: Applies a fixed threshold to create a binary image.
- **Median Filter**: Smooths the image to reduce noise while preserving edges.
- **Min Filter**: Highlights darker regions in the image.
- **Max Filter**: Highlights brighter regions in the image.

## Requirements

- Python 3.x
- Libraries:
  - `opencv-python`
  - `numpy`
  - `Pillow` (PIL)

Install the required packages with:
```bash
pip install opencv-python numpy pillow
```

## Filter Descriptions and Practical Use Cases

1. **Otsu Thresholding**:
   - **Description**: An automatic thresholding algorithm that calculates an optimal threshold value based on histogram analysis, separating the image into foreground and background.
   - **Application**: Widely used in segmentation tasks where objects need to be separated from the background, such as in medical imaging to highlight tumors, or in industrial inspection for defect detection.

2. **Fixed Thresholding**:
   - **Description**: A simple threshold filter that converts pixel values above a fixed level (127) to white and those below to black.
   - **Application**: Suitable for images with clear object-background separation, such as document scanning or black-and-white image processing.

3. **Median Filter**:
   - **Description**: A filter that replaces each pixel's value with the median of its neighboring pixels, effectively reducing noise while maintaining edge clarity.
   - **Application**: Often used in image preprocessing before segmentation or recognition tasks, such as in surveillance or medical imaging to remove minor noise.

4. **Min Filter**:
   - **Description**: A morphological erosion operation that replaces each pixel with the minimum value among its neighbors, effectively reducing bright regions.
   - **Application**: Useful for removing small white noise, thinning light lines, and enhancing object boundaries, particularly in scanned document processing or in detecting minor bright defects.

5. **Max Filter**:
   - **Description**: A morphological dilation operation that replaces each pixel with the maximum value of its neighbors, expanding bright regions.
   - **Application**: Used to fill small dark holes or enhance bright objects, such as in defect detection, texture analysis, or edge detection.

## How to Run the Application

1. **Run the application**:
    ```bash
    python KG2.py
    ```
2. **Load an Image**:
    - Click the "Load Image" button to select a grayscale image for processing.

3. **Apply Filters**:
    - Use the corresponding buttons to apply various image processing filters:
      - **Otsu Thresholding**: Automatically segments objects and background.
      - **Fixed Thresholding**: Applies a fixed threshold for binarization.
      - **Median Filter**: Reduces noise while preserving edges.
      - **Min Filter**: Diminishes bright areas.
      - **Max Filter**: Enhances bright areas.

4. **View Results**:
    - After applying a filter, the result is displayed on the screen, replacing the original image view.

## File Structure

- `KG2.py`: The main application file containing the GUI and image processing logic.

# Rasterization Graphics Application

This graphical application, built with Python's Tkinter and Matplotlib, visualizes different line and circle rasterization algorithms. It allows users to input coordinates and radius values, select an algorithm, and draw lines or circles using specified algorithms. The interface also provides options to clear specific lines or all shapes from the graph.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Error Handling](#error-handling)
- [Acknowledgements](#acknowledgements)

## Features
- **Draw Lines and Circles**: Supports different rasterization algorithms for lines and circles, including:
  - Step-by-Step Line
  - Digital Differential Analyzer (DDA) Line
  - Bresenham Line
  - Bresenham Circle
- **Performance Measurement**: Calculates and displays the execution time of each algorithm.
- **Clear Options**: Remove individual lines or circles, or clear all shapes from the graph.
- **Visual Customization**: Graph grid with adjustable markers and axis settings.

## Installation
### Requirements
- Python 3.x
- Libraries:
  - `tkinter`
  - `ttk` from Tkinter
  - `matplotlib`

### Setup
1. Clone the repository or download the code file.
2. Install Matplotlib if it is not already installed:
   ```bash
   pip install matplotlib
   ```
3. Run the program:
   ```bash
   python KG3.py
   ```

## Usage
1. **Input Coordinates and Radius**:
   - Enter `X1`, `Y1`, `X2`, and `Y2` values for line algorithms.
   - For circles, enter `X1`, `Y1`, and a `Radius`.
2. **Select an Algorithm**:
   - Click on the algorithm button you want to execute. 
   - The program will compute and display the points on the graph and show the execution time in milliseconds.
3. **Clear Lines or Circles**:
   - Use the "Clear" buttons to remove specific lines or the entire graph.

## Algorithms
### Step-by-Step Line
Computes line points incrementally by calculating intermediate points from `X1` to `X2`. Adjusts for slope and intercept.

### DDA (Digital Differential Analyzer) Line
Divides the line into steps based on the greatest change between `dx` and `dy`, generating points incrementally.

### Bresenham Line
A more optimized line rasterization algorithm using integer calculations to reduce error accumulation.

### Bresenham Circle
A circle-drawing algorithm that plots points symmetrically to form a circle with minimal computational effort.

## Error Handling
- **Input Validation**: Checks for integer inputs. If invalid values are entered, an error message will display below the input fields.
- **Execution Time Display**: Execution time is displayed only if the algorithm runs successfully.

## Acknowledgements
- Algorithms are based on common rasterization methods for graphics.
- Developed using Python and Tkinter for GUI, with Matplotlib for graphical display.

## Contributing

If you would like to contribute to this project, feel free to submit issues or pull requests. Enhancements such as better color conversion algorithms, additional color models (like HSV or LAB), or a more advanced user interface are welcome.

---

Enjoy exploring color theory with this interactive tool!

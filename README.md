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
    git clone https://github.com/your-username/color-models-app.git
    ```

2. Navigate to the directory where the script is saved:
    ```bash
    cd color-models-app
    ```

3. Run the program:
    ```bash
    python color_models.py
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

## Contributing

If you would like to contribute to this project, feel free to submit issues or pull requests. Enhancements such as better color conversion algorithms, additional color models (like HSV or LAB), or a more advanced user interface are welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy exploring color theory with this interactive tool!

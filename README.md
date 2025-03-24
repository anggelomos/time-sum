
A small CLI utility for adding multiple time values in `HH.MM` format.

## Usage

When you run the tool, it will prompt you to enter time values one by one. After each entry, it displays the running total.

1. Enter each time value in the format `HH.MM` (e.g., `2.30` for 2 hours and 30 minutes)
2. Press Enter after each value
3. The running total will be displayed after each entry
4. Enter a single period (`.`) to finish and see the final total

Example session:
```
Enter the times and press enter after each one. Press . to finish.
1.30
  =1.5
2.15
  =3.75
0.45
  =4.5
.
```

## Building the Executable

To create a standalone executable that can be run without Python installed:

1. Make sure you have Python and pip installed
2. Install PyInstaller:
   ```
   pip install pyinstaller
   ```
3. Navigate to the project directory
4. Run PyInstaller with the following command:
   ```
   pyinstaller --onefile --name time_calculator app.py
   ```

5. Find the executable in the `dist` directory

## Requirements

- Python 3.8+ (for running from source)
- No external dependencies required

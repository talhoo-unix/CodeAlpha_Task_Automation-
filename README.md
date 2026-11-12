# JPG File Automation Using Python

## Project Description
This project is a simple file automation script developed as part of the CodeAlpha Python Internship.

The program automatically moves all `.jpg` image files from a specified source folder to a destination folder. It saves time by eliminating the need to manually move image files.

## Features
- Moves JPG images from one folder to another
- Automatically creates the destination folder if it does not exist
- Checks whether the source folder exists
- Prevents overwriting files with the same name
- Displays the total number of files moved
- Leaves other file types unchanged

## Technologies Used
- Python
- OS module
- Shutil module
- Argparse module

## How to Run

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in the terminal.
4. Run the following command:

```bash
python python_script_automation.py source dest
```

**Note:** Replace `source` and `dest` with your actual folder names if they are different.

## Example

If the source folder contains:
- photo1.jpg
- photo2.jpg
- presentation.pptx

After running the program:
- Both JPG images are moved to the destination folder.
- The PowerPoint file remains in the source folder.

## Internship
Developed as part of the CodeAlpha Python Internship.
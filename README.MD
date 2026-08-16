File Organizer

A simple Python script that automatically organizes files in a folder based on their file type (extension).

What it does

Scans a target folder and moves each file into a subfolder based on its extension:


Extension	Destination Folder
.jpg, .jpeg, .png, .gif	Images
.pdf, .docx, .txt, .xlsx	Documents
.mp4, .mov	Videos
.mp3	Music
.zip	Compressed
.exe    Applications
anything else	Others
Requirements
Python 3.x (no extra libraries needed — uses only built-in modules)
Usage
Option 1: Run manually
bash
samorganizer.py

You'll be prompted to enter the full path of the folder you want to organize.

Option 2: Run with a target folder as argument
bash
python duzenleyici.py "C:\Users\YourName\Downloads"
Option 3: Windows shortcut (.bat file)

A samorganizer.bat file is included, which automatically organizes your Downloads folder with a single double-click. It uses the %USERPROFILE% environment variable, so it works on any Windows account without editing the path.

Example output
Moved: photo.jpg -> Images/
Moved: report.pdf -> Documents/
Moved: song.mp3 -> Music/

Total 3 files organized.
Notes
The script moves files, it does not copy them — there is no undo.
It's recommended to test it on a sample/test folder before running it on important directories.
Files already inside a subfolder (e.g. Images/) are left untouched on future runs.
Possible future improvements
Add a log file to keep a history of moved files
Add a "dry run" mode to preview changes before moving files
Watch a folder continuously and organize new files automatically (using watchdog)

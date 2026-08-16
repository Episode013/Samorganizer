import os 
import shutil
import sys

Folders = {
    ".jpg": "Images",
    ".png": "Images",
    ".jpeg": "Images",
    ".gif": "Images",
    ".tif": "Images",
    ".ico": "Images",
    ".pdf": "Documents",
    ".udf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".mp3": "Audios",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".exe": "Applications",
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"The folder path '{folder_path}' does not exist.")
        return

    files = os.listdir(folder_path)
    moved_count = 0

    for file_name in files:
        full_path = os.path.join(folder_path, file_name)

        if os.path.isdir(full_path):
            continue
        _, extension = os.path.splitext(file_name)
        extension = extension.lower()

        if extension in Folders:
            target_folder_name = Folders[extension]
        else:
            target_folder_name = "Others"

        target_folder_path = os.path.join(folder_path, target_folder_name)
        os.makedirs(target_folder_path, exist_ok=True)

        destination_path = os.path.join(target_folder_path, file_name)
        shutil.move(full_path, destination_path)

        print(f"Moved: {file_name} -> {target_folder_name}/")
        moved_count += 1
        print(f"\nTotal {moved_count} files organized.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        target_folder = input("Enter the full path of the folder to organize: ")
    organize_files(target_folder)

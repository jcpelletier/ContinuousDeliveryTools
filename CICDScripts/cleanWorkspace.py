import os
import sys

def clean_folder(folder_path):
    if os.path.exists(folder_path):
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
        os.rmdir(folder_path)
        print(f"Step 1: Cleaned '{folder_path}'")
    else:
        print(f"'{folder_path}' does not exist. No cleanup needed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <folder_path>")
    else:
        folder_path = sys.argv[1]
        clean_folder(folder_path)

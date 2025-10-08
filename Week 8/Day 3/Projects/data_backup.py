import os
import shutil
import json

def is_safe_path(basedir, path):
    # Ensure the path is within the basedir
    return os.path.commonpath([basedir, path]) == os.path.abspath(basedir)

def backup_file(src_path, dest_dir, src_dir):
    filename = os.path.basename(src_path)
    ext = os.path.splitext(filename)[1].lower()
    dest_path = os.path.join(dest_dir, filename)

    # Check for path traversal
    if not is_safe_path(src_dir, src_path):
        print(f"Unsafe path detected: {src_path}")
        return

    if ext == '.txt' or ext == '.csv':
        shutil.copy2(src_path, dest_path)
    elif ext == '.json':
        with open(src_path, 'r') as f:
            data = json.load(f)
        with open(dest_path, 'w') as f:
            json.dump(data, f, indent=2)
    else:
        print(f"Unsupported file format: {filename}")

def backup_directory(src_dir, dest_dir):
    src_dir = os.path.abspath(src_dir)
    dest_dir = os.path.abspath(dest_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        if os.path.isfile(src_path):
            backup_file(src_path, dest_dir, src_dir)

if __name__ == "__main__":
    source = input("Enter source directory: ")
    backup = input("Enter backup directory: ")
    backup_directory(source, backup)
import os
import shutil

def copy_and_exclude(src, dst):
    for root, dirs, files in os.walk(src):
        # Create the destination directory structure
        rel_root = os.path.relpath(root, src)
        dest_dir = os.path.join(dst, rel_root)

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Exclude 'node_modules' in each subdirectory
        if 'node_modules' in dirs:
            dirs.remove('node_modules')

        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)

# Usage example:
source_directory = '/media/acer/Aayush/copy-script'
destination_directory = '/media/acer/Aayush/copy-script/all-copied/others/copy-script'
copy_and_exclude(source_directory, destination_directory)

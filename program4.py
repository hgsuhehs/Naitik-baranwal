import os

# Specify the directory path (change to desired path)
directory_path = '.'  # current directory

try:
    # List all files and directories in the specified directory
    contents = os.listdir(directory_path)
    print(f'Contents of "{directory_path}":')
    for item in contents:
        print(item)
except FileNotFoundError:
    print('Directory not found.')
except PermissionError:
    print('Permission denied.')

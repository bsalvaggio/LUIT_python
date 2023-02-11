#!/usr/bin/env python3
# Create a script that will list all files in the current working directory and will extract info,
#     such as name and size, as well as the modification time, access time, creation time, file type,
#     file permissions, owner, and group.

import os
import time

# Get a list of all files in the current working directory
files = os.listdir(os.getcwd())

# Initialize an empty list to store dictionaries of file information
file_info = []

# Loop through the list of files
for file in files:
    # Get the file name and size
    file_name = file
    file_size = os.path.getsize(file)
    modification_time = time.ctime(os.path.getmtime(file))
    access_time = time.ctime(os.path.getatime(file))
    creation_time = time.ctime(os.path.getctime(file))

    # Determine if the file is a regular file or a directory
    if os.path.isfile(file):
        file_type = "file"
    elif os.path.isdir(file):
        file_type = "directory"
    else:
        file_type = "other"

    # Get information about the file's permissions
    file_stats = os.stat(file)
    file_permissions = oct(file_stats.st_mode)[-3:]
    file_owner = file_stats.st_uid
    file_group = file_stats.st_gid

    # Add a dictionary of the file information to the list
    file_info.append({
        'name': file_name,
        'size': file_size,
        'modification_time': modification_time,
        'access_time': access_time,
        'creation_time': creation_time,
        'type': file_type,
        'permissions': file_permissions,
        'owner': file_owner,
        'group': file_group
    })

# Print the list of dictionaries
print(file_info)

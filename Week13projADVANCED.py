#!/usr/bin/env python3

import os
import time

def get_file_info(path='.'):
    # Get a list of all files in the specified path
    files = os.listdir(path)

    # Initialize an empty list to store dictionaries of file information
    file_info = []

    # Loop through the list of files
    for file in files:
        # Get the file name and size
        file_path = os.path.join(path, file)
        file_name = file
        file_size = os.path.getsize(file_path)
        modification_time = time.ctime(os.path.getmtime(file_path))
        access_time = time.ctime(os.path.getatime(file_path))
        creation_time = time.ctime(os.path.getctime(file_path))

        # Determine if the file is a regular file, a directory, or something else
        if os.path.isfile(file_path):
            file_type = "file"
        elif os.path.isdir(file_path):
            file_type = "directory"
        else:
            file_type = "other"

        # Get information about the file's permissions
        file_stats = os.stat(file_path)
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
        
        # If the file is a directory, recursively call the function with that directory as the path
        if os.path.isdir(file_path):
            file_info.extend(get_file_info(file_path))

    # Return the list of dictionaries
    return file_info

# Call the function and store the result in a variable
file_info = get_file_info()

# Print the list of dictionaries (on separate lines)
for file in file_info:
    print("Name: ", file['name'])
    print("Size: ", file['size'])
    print("Modification Time: ", file['modification_time'])
    print("Access Time: ", file['access_time'])
    print("Creation Time: ", file['creation_time'])
    print("Type: ", file['type'])
    print("Permissions: ", file['permissions'])
    print("Owner: ", file['owner'])
    print("Group: ", file['group'])
    print("\n")

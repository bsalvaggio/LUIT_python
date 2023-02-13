#!/usr/bin/env python3
"""
# This module is used to extract information about files in a directory,
#     including their name, size, modification time, access time, creation time,
#     file type, file permissions, owner, and group.
"""

import os
import time

def get_file_info(path='.'):
    """
    Get information about files in a given path.

    Args:
    path (str, optional): The path to the directory to get file information from.
         Defaults to '.' (the current working directory).

    Returns:
    list: A list of dictionaries, where each dictionary contains information about a file in the directory.
    """

    if path is None:
        path = os.getcwd()

    file_info = []

    for dirpath, filenames in os.walk(path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_name = file
            file_size = os.path.getsize(file_path)
            modification_time = time.ctime(os.path.getmtime(file_path))
            access_time = time.ctime(os.path.getatime(file_path))
            creation_time = time.ctime(os.path.getctime(file_path))

            if os.path.isfile(file_path):
                file_type = "file"
            elif os.path.isdir(file_path):
                file_type = "directory"
            else:
                file_type = "other"

            file_stats = os.stat(file_path)
            file_permissions = oct(file_stats.st_mode)[-3:]
            file_owner = file_stats.st_uid
            file_group = file_stats.st_gid

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

    return file_info

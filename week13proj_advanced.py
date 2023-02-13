#!/usr/bin/env python3

# ADVANCED: Modify the script into a function such that any path can be passed as a parameter.
#     This parameter should be optional and should default to working directory when the variable is not passed
#     The function should then create the list of dictionaries anout files from that path.
#     The function should also return information on files nested in folders (recursive)

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
     modification__time = time.ctime
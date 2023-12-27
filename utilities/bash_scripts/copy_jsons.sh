#!/bin/bash

# Check for minimum required number of arguments
if [ $# -lt 3 ]; then
    echo "Usage: $0 <folder_path> <source_file> <number_of_copies>"
    exit 1
fi

folder_path=$1      # Folder path
source_file=$2      # Source file to copy
number_of_copies=$3 # Number of copies to make

# Check if the folder exists
if [ ! -d "$folder_path" ]; then
    echo "The specified folder does not exist."
    exit 1
fi

# Check if the source file exists
if [ ! -f "$source_file" ]; then
    echo "The source file does not exist."
    exit 1
fi

# Copy the source file to the specified number of copies
for i in $(seq 1 $number_of_copies); do
    cp "$source_file" "$folder_path/$(basename "$source_file" .json)-$i.json"
done

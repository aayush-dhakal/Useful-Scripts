#!/bin/bash

# Change to the directory containing the files
cd /media/acer/Aayush/photos

# Rename all files, replacing _ with -
for file in *; do
    new_name=$(echo "$file" | tr '_' '-') # replace _ with -
    # new_name=$(echo "$file" | tr -d "'") # delete '
    # new_name=$(echo "$file" | tr -d ",") # delete ,
    # new_name=$(echo "$file" | tr -d "!") # delete !
    # new_name=$(echo "$file" | tr -d "»") # delete »
    # new_name=$(echo "$file" | tr -d "@") # delete @
    mv "$file" "$new_name"
done

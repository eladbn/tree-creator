#!/usr/bin/env python3
import os
import re
import sys

def parse_tree_and_create_structure(tree_text):
    """
    Parse the tree structure text and create corresponding folders and files.
    """
    lines = tree_text.strip().split('\n')
    
    # Extract the root directory name from the first line
    root_dir = lines[0].rstrip('/')
    
    # Create the root directory if it doesn't exist
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)
        print(f"Created directory: {root_dir}")
    
    current_path = [root_dir]
    prev_indent_level = 0
    
    # Process each line after the root
    for line in lines[1:]:
        # Skip empty lines
        if not line.strip():
            continue
            
        # Extract the indentation level based on the characters ├, │, └, etc.
        indent_match = re.match(r'^([ │]*)([├└])(──)', line)
        if not indent_match:
            continue
            
        indent_str = indent_match.group(1)
        indent_level = len(indent_str) // 2 + 1  # Each level is represented by 2 characters (│ )
        
        # Extract the item name, removing any trailing comments
        item_name = line[len(indent_match.group(0)):].split('#')[0].strip()
        
        # Handle the case where indentation decreases
        if indent_level < prev_indent_level:
            # Remove directories from the current path
            current_path = current_path[:indent_level]
        
        # Handle the case where we're at a new level
        if indent_level == prev_indent_level:
            current_path.pop()  # Remove the last item
        
        # Determine if this is a file or directory
        is_directory = item_name.endswith('/')
        
        # Clean up the name (remove trailing slash for directories)
        clean_name = item_name.rstrip('/')
        
        # Handle special cases where ** might be in the filename (like **init**.py)
        clean_name = clean_name.replace('**', '__')
        
        # Create the full path
        full_path = os.path.join(*current_path, clean_name)
        
        if is_directory:
            # Create directory
            if not os.path.exists(full_path):
                os.makedirs(full_path)
                print(f"Created directory: {full_path}")
            current_path.append(clean_name)
        else:
            # Create empty file
            if not os.path.exists(full_path):
                with open(full_path, 'w') as f:
                    pass  # Create an empty file
                print(f"Created file: {full_path}")
            current_path.append(clean_name)
        
        prev_indent_level = indent_level

def main():
    print("Please paste your tree structure below.")
    print("When finished, type 'DONE' on a new line and press Enter:")
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "DONE":
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\nInput interrupted. Exiting.")
            sys.exit(1)
    
    tree_text = "\n".join(lines)
    
    if not tree_text.strip():
        print("No input provided. Exiting.")
        sys.exit(1)
    
    parse_tree_and_create_structure(tree_text)
    print("Tree structure created successfully!")

if __name__ == "__main__":
    main()
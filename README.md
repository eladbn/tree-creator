# Tree Creator Script

A Python utility script that creates directory structures and empty files from a text-based tree representation.

## Overview

`tree_creator.py` is a simple but powerful tool that allows you to quickly generate complex folder and file structures based on a visual tree diagram. Instead of manually creating directories and files one by one, you can paste a tree structure and the script will automatically generate all the necessary folders and files for you.

## Features

- Creates nested directories with arbitrary depth
- Generates empty files at specified locations
- Handles special filenames (e.g., `__init__.py` files in Python)
- Provides detailed feedback during the creation process
- Works on all major operating systems (Windows, macOS, Linux)
- Simple, interactive command-line interface

## Requirements

- Python 3.6 or higher

## Installation

No installation is required. Simply download the `tree_creator.py` script to your computer.

## Usage

1. Save the script as `tree_creator.py`
2. Run the script:
   ```
   python tree_creator.py
   ```
3. Paste your tree structure when prompted
4. Type `DONE` on a new line and press Enter when finished
5. The script will create all directories and files in your current working directory

## Input Format

The script expects a tree structure in the following format:

```
root_folder/
├── subfolder1/
│   ├── file1.txt
│   └── file2.txt
└── subfolder2/
    └── file3.txt
```

### Format Rules:

- The first line should be the root directory name (with or without a trailing slash)
- Use standard tree characters (`├`, `│`, `└`, `──`) for the structure
- Directory names should end with a `/` (slash)
- File names should not end with a `/`
- Comments can be added after `#` and will be ignored

## Example

Input:
```
my_project/
├── src/
│   ├── __init__.py
│   └── main.py
└── docs/
    └── README.md
```

This will create:
- A directory called `my_project`
- A subdirectory called `src` inside `my_project`
- An empty file called `__init__.py` inside `my_project/src`
- An empty file called `main.py` inside `my_project/src`  
- A subdirectory called `docs` inside `my_project`
- An empty file called `README.md` inside `my_project/docs`

## Limitations

- The script creates empty files only. No content is added to the files.
- Special characters in filenames should be avoided.
- Very deep nested structures (more than 100 levels) might cause issues.

## License

This script is released under the MIT License. Feel free to modify and distribute it.

## Contributing

Contributions are welcome! Feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvements.

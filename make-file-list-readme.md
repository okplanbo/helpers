File Listing Script
===================

Overview
--------

This Windows batch script lists all files in the current directory and subdirectories, writes their names to a text file (`files_list.txt`), and handles Cyrillic characters by setting the code page to UTF-8.

Requirements
------------

-   Operating System: Windows
-   Command Prompt: Batch scripting environment

Usage
-----

1.  Save the script in a folder containing the files you want to list.
2.  Double-click the script file or run it from the command prompt:

    `script_name.bat`

Output
------

-   The script outputs a file named `files_list.txt` in the same directory.
-   This file contains the list of all files processed, with their full paths.
-   The script also displays the number of files processed in the command prompt window.

Notes
-----

-   The script periodically clears the screen to update the file processing count every 10 files to keep the output manageable.
-   If `files_list.txt` already exists, it will be deleted at the start of the script to ensure a fresh start.

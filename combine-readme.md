
Text File Combiner and Encoder Script
=====================================

Overview
--------

This script is designed to combine multiple text files into a single file, while ensuring all text is uniformly encoded in UTF-8. It processes all `.txt` files in the current directory, checks and converts their encoding if necessary, appends their content along with metadata (file name and last modification date) to a combined text file named `combined.txt`.

Requirements
------------

-   Operating System: Linux or Unix-like operating system
-   Shell: Bash
-   Tools:
    -   `iconv`: For converting file encodings.
    -   `file`: For determining the MIME type and character encoding of files.
    -   `awk`: For processing text.
    -   `stat`: For retrieving file metadata.

Make sure these tools are installed on your system. They are typically pre-installed in most Linux distributions.

Usage
-----

1.  Place the script in a directory with `.txt` files you want to combine.
2.  Make the script executable if it isn't already:

    `chmod +x script_name.sh`

3.  Run the script:

    `./script_name.sh`

Output
------

-   The script generates a single file named `combined.txt` in the same directory.
-   Each section in `combined.txt` starts with the original file's name and last modification date, followed by the content of the file.
-   Files are separated by blank lines for clarity.

Notes
-----

-   If the encoding of a text file is not UTF-8, it will be converted using `iconv`. The script currently assumes a source encoding of Windows-1251 for conversion. Adjust this as necessary to match the encoding of your files.
-   Temporary `.utf8` files are created during the processing but are cleaned up after the script completes.

Example
-------

Here's what part of the `combined.txt` might look like:

`File: example1.txt
Modification Date: 2023-04-01 12:00:00
Content of example1.txt...

File: example2.txt
Modification Date: 2023-04-01 12:10:00
Content of example2.txt...`

* * * * *

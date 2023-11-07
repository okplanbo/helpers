#!/bin/bash

output_file="combined.txt"

# Create an empty output file
> "$output_file"

for file in *.txt; do
  # Determine the encoding of the file
  encoding=$(file -i "$file" | awk -F'=' '{print $2}')
  # Get file name, last modification date
  file_name=$(basename "$file")
  modification_date=$(stat -c %y "$file")
  
  # Convert the file to UTF-8 if it's not already
  if [[ "$encoding" != "utf-8" ]]; then
    # Specify the source encoding (e.g., Windows-1251) in the iconv command
    iconv -f WINDOWS-1251 -t utf-8 "$file" > "$file.utf8"
    file="$file.utf8"
  fi

  # Combine file info with the output file
  echo "File: $file_name" >> "$output_file"
  echo "Modification Date: $modification_date" >> "$output_file"
  echo "" >> "$output_file"
  cat "$file" >> "$output_file"
  echo "" >> "$output_file"
  echo "" >> "$output_file"
done

# Clean up temporary files
rm -f *.utf8

echo "All files combined and encoded to UTF-8 in $output_file"

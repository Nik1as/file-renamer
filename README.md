# File Renamer

````
usage: file_renamer.py [-h] [-p PATTERN] [-s {size,creation,access,modified}] [-o {asc,desc}] folder

positional arguments:
  folder                Folder with the files you want to rename

options:
  -h, --help            show this help message and exit
  -p PATTERN, --pattern PATTERN
                        Pattern for the new file names. # gets replaced by a number.
  -s {size,creation,access,modified}, --sort-by {size,creation,access,modified}
                        Sort the files
  -o {asc,desc}, --order {asc,desc}
                        Sort the files ascending or descending
````
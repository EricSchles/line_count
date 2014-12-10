#Line Count

This project counts the total number of lines of a given file extension across a file-system.  The intended use-case is to pass in all relevant directories with code (for example .py) or txt files.  The sum of all files is returned by the main function.  This is will be part of a suite of tools that will tell you how you are doing on your local file system.

#To use:

python line_count/counter.py [extension] [list of root directories]

specific examples:

python line_count/counter.py .py ~ /mnt/hfgs/

python line_count/counter.py .py
--if no directory is passed in home directory is run by default



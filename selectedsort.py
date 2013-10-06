#!/usr/bin/python
import re

# NOTES
	# This script will enable for easier importing of data into a graphing program
	# This script reads from sorted.txt
	# This script will also remove the ':' after each torrent id

sortedfile = open("sorted.txt", "r")
selectedsortedfile = open("selectedsorted.txt", "w")

regex = re.compile("Error")

for line in sortedfile:
	if regex.search(line) == None:
		line = line.replace(":", "")
		selectedsortedfile.write(line)

selectedsortedfile.close()
selectedsortedfile = open("selectedsorted.txt", "r")


sortedfile.close()
selectedsortedfile.close()
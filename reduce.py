#!/usr/bin/python
import re

# NOTES
	# This script will output the results to the terminal

total = 0

sortfile = open("sorted.txt", "r")

# Number of Deleted Torrents
regex = re.compile("Error")
errors = regex.findall(sortfile.read())
print "Number of Deleted Torrents: " + str(len(errors))

sortfile.close()
sortfile = open("sorted.txt", "r")

# Total Size of Torrents
regex = re.compile("(?<=\:\s)[0-9]+")
sizes = regex.findall(sortfile.read())
for size in sizes:
	total = total + int(size)
print "Total Size of Torrents: " + str(total)

sortfile.close()

# Number of Torrents
torrents = len(sizes)
print "Number of Torrents: " + str(torrents)

# Average Size of Torrents
average = total / torrents
print "Average Size of Torrents: " + str(average)

sortfile.close()
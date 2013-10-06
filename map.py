#!/usr/bin/python
import re

# NOTES
	# If you have done the collecting in parts, run sort.py in between collections, and copy sorted.txt into one of the original files before
	
	# Run the following in a command line prior to running this script, so the files are numbered (remove any other txt files from the directory first):
	#index=0;
	#for name in *.txt
	#do
	#    cp "${name}" "${index}.txt"
	#    index=$((index+1))
	#done

i = 0
k = 0
lines = []

while i <= 199: # Set this to the highest number file name
	originalfile = open(str(i) + ".txt", "r")
	
	for line in originalfile:
		lines.append(line)
	
	originalfile.close()
	
	i = i + 1

lines.sort();

sortfile = open("sorted.txt", "w")

for line in lines:
	sortfile.write(line)

sortfile.close()

sortfile = open("sorted.txt", "r")

regex = re.compile("[0-9]+(?=\:)")
numbers = regex.findall(sortfile.read())

while k < len(numbers) - 1:
	if int(numbers[k]) + 1 != int(numbers[k+1]):
		print "A torrent is missing around " + numbers[k] + "."
	k = k + 1

sortfile.close()
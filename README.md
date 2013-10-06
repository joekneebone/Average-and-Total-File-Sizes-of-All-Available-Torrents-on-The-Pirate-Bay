Average and Total File Sizes of All Available Torrents on The Pirate Bay
========================================================================

This tool allows you to calculate the average and total file sizes of all available torrents on The Pirate Bay.

This tool requires that Ruby and Python are installed on your computer. This tool also requires that you have the ThePirateBay Ruby Gem (https://github.com/emnl/thepiratebay).

First, run the collect.rb script. This script will run forever, so it must be manually stopped when the most recent torrent has been collected. Next, run the map.py script. This will order and collate the data into a single file. Next, run reduce.py. This will provide you with the number of deleted torrents, the the total file size of all available torrents (in bytes), the total number of available torrents, and the average size of all available torrents (in bytes).

To create a graph, first run selectedsort.py. This will create a new file, with the deleted torrents removed. This file can then be imported into a graphing program, such as DataGraph (http://www.visualdatatools.com/DataGraph/). This file cannot be imported into Microsoft Excel, due to the number of torrents.

An example graph has been included in this repository.

Further details can be found at the beginning of each script.
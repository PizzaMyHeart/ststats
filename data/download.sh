#!/bin/bash

echo 'Downloading competition ratio PDFs ...'

wget --user-agent=\
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36' \
--referer='https://specialtytraining.hee.nhs.uk/Competition-Ratios' \
-nd -r -l2 -w 1 -A pdf -e robots=off \
https://specialtytraining.hee.nhs.uk/Competition-Ratios

# wget options
# ---------------
# -nd: Save all files to current directory. 
# -r: Recursive download (download linked documents).
# l2: Maximum depth of 2 (download documents linked from first page only).
# -w1: Wait 1 second between each download.
# -A pdf: Download PDFs only.
# -e robots=off: Without this option only PDFs in /portals/ are downloaded. Not sure why.

echo 'Download complete.'


#!/bin/bash
#find . -name title.txt | xargs cat >alltitles.txt
find . -name title.txt | xargs head -n 1 > allheaders.txt

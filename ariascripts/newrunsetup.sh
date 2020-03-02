#!/bin/bash
xml=$1
nam=$2
remote_dir=/home/nmrbox/tportlock/aria/${nam}/
run=$(echo $1 | sed 's/[^0-9]*//g') 

echo "cd $remote_dir && /usr/software/bin/aria2 -s run${run}.xml && /usr/software/bin/aria2 --output=run${run}.log $xml > /dev/null 2>&1 &" > $nam-run$run.sh &&
chmod a+x $nam-run$run.sh

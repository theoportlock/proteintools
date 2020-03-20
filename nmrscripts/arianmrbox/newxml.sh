#!/bin/bash
prevrun=$(echo $1 | sed 's/[^0-9]*//g') 
run=$(($prevrun+1)) 

cp $1 run$run.xml && 
sed -i -e "s/run${prevrun}/run${run}/g" -e "s/\"${prevrun}\"\ file_root/\"${run}\"\ file_root/g" -e "s/run${prevrun}analysis/run${run}analysis/g" run${run}.xml

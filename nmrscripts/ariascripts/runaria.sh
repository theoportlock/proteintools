#!/bin/bash
nam="lspd_n0"
run=$(echo $1 | sed 's/[^0-9]*//g') 
remote_dir=/home/nmrbox/tportlock/aria/${nam}/
remote_addr='tportlock@tportlock.nmrbox.org'
xml_script=$1
ccpn_project=$2
run_script=$3

scp -r $ccpn_project $remote_addr:$remote_dir &&
scp -r $xml_script $remote_addr:$remote_dir
scp -r $run_script $remote_addr:$remote_dir
ssh $remote_addr "${remote_dir}$3"
sleep 4h
ssh ${remote_addr} "cd ${remote_dir} && mv run${run}analysis $3 run${run}.log run${run}.xml run${run}" &&
scp -r ${remote_addr}:${remote_dir}/run${run} . &&
ssh tportlock@tportlock.nmrbox.org "rm -r /home/nmrbox/tportlock/aria/${nam}/run${run}"

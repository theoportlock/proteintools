#!/bin/bash
nam="lspd_n0"
run=$(echo $1 | sed 's/[^0-9]*//g') &&

remote_dir=/home/nmrbox/tportlock/aria/${nam}/
remote_addr='tportlock@tportlock.nmrbox.org'
xml_script=$1
ccpn_project=$2

#scp -r $ccpn_project $remote_addr:$remote_dir &&
#scp -r $xml_script $remote_addr:$remote_dir

ssh $remote_addr < echo "cd $remote_dir && aria2 -s run${run}.xml"
       	#aria2 --output=run${run}.log run${run}.xml > /dev/null 2>&1 &"

EXITCODE=$?
if [ $EXITCODE -eq 0 ]
then
	echo "it worked"
	#ssh ${remote_dir} "cd ${remote_dir} && mv run${run}analysis run${run}.log run${run}.xml run${run}" &&
	#scp -r ${remote_addr}:${remote_dir}/run${run} . &&
	#ssh tportlock@tportlock.nmrbox.org "rm -r /home/nmrbox/tportlock/aria/${nam}/${run}"
elif [ $? == 255 ]
	echo "Unable to connect"
	exit 2
else
	exit $EXITCODE
then

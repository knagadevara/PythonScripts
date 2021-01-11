#!/usr/bin/env bash

myPATH='/tmp'
fileLOC="${1}"
PingHOST="ping -c 4 -w 10"
OutFile="${myPATH}/PingOutput.txt"
UsageDialog="This tool will only take single parameter, please find the below USAGE:\n\n\t ${0} <Path to HostsFile>\n"


if [[ ${#} -ne 1 ]]
	then
	echo -e ${UsageDialog}
	exit 1
fi

if [[ ! -f "${myPATH}/${fileLOC}" ]]
	then
		echo "File not there"
		exit 2
	else
		touch ${OutFile}
	fi

for NewHosts in $( cat "${myPATH}/${fileLOC}" )
	do
	${PingHOST} ${NewHosts} &>/dev/null
	PingStatus=`echo $?`
	if [[ $PingStatus -eq 0 ]]
		then
			echo "${NewHosts} PING SUCCESS" >> ${OutFile}
		elif [[ $PingStatus -eq 2 ]]
		then
			echo "${NewHosts} DNS FAILED" >> ${OutFile}
		else
			echo "${NewHosts} PING FAILED" >> ${OutFile}
	fi
done

cat $OutFile
rm -rf $OutFile

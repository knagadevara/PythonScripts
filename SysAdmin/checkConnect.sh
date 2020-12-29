#!/usr/bin/env bash

myPATH='/tmp'
fileLOC="${1}"
PingHOST="ping -c 4 -w 3"
OutFile="${myPATH}/PingOutput.txt"
touch ${OutFile}
UsageDialog="This tool will only take single parameter, multiple given, please find the below USAGE.\n\t:./${0} <Path to HostsFile>"


if [[ ${#} > 1 ]]
then
echo -e ${UsageDialog}
exit 1
fi

for NewHosts in $( cat "${myPATH}/${fileLOC}" )

do
${PingHOST} ${NewHosts} 2 >/dev/null
PingStatus=$?

if [[ $PingStatus > 0 ]]
then
echo "${NewHosts} Network-PING SUCCESS" >> ${OutFile}
else
echo "${NewHosts} Network-PING FAILED" >> ${OutFile}
fi

done
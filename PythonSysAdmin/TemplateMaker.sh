#!/usr/bin/bash

lang=$1
name=$2
PyWRKd="$HOME/PythonScripts"
BinWRKd="$HOME/bin"

## Check if file already exists
if [[ -f $name ]] ; then
  echo -en "Exiting as File name already exists \nPlease hoose a new filename \n"
  exit 1
fi

## Checking if the directory is present
if [[ ! -d ${PyWRKd} ]] ; then
  echo "NO Parent Directory"
  mkdir $PyWRKd
  echo "Created"
elif [[ ! -d ${BinWRKd} ]] ; then
  echo "NO Personal Binary Linker"
  mkdir ${BinWRKd}
  echo "Created"
fi

function usage()
{
  echo 'Request you to provide the below as arguments for the file:'
  echo -en "\n $0 python <name of file> \n \t for PYTHON... \n"
  echo -en "\n $0 bash <name of file> \n \t for BASH...\n"
  echo -en "\n $0 ruby <name of file> \n \t for RUBY...\n"
}

function checkFrmt(){
if [[ $lang == 'python' ]] ; then
  sbang="#!$(which python3)"
  ext='py'
elif [[ $lang == 'bash' ]] ; then
  sbang="#!$(which bash)"
  ext='sh'
elif [[ $lang == 'ruby' ]] ; then
  sbang="#!$(which  ruby)"
  ext='rb'
else
  flg=3
  echo "Failed to create the file"
  usage
fi
}

function TemplateContent(){
  echo ${sbang}
  echo -en "\n"
  echo -en "#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#"
  echo -en "\n"
  echo -en "\n\t# By Author: $USER"
  echo -en "\n\t# Date: $(date)"
  echo -en "\n\t# Scripting Language: $lang"
  echo -en "\n\t# Copyright:: $(date +%Y), The Authors, All Rights Reserved. \n"
  echo -en "\n"
  echo -en "#--- --- --- --- --- --- --- --- --- ---##--- --- --- --- --- --- --- --- --- ---#"
  echo -en "\n"
  echo -en "\n"
}

function enb(){
export PATH=${BinWRKd}:$PATH
checkFrmt
if [[ $flg -ne 0 ]] ; then
    echo "Exiting Script"
    exit 1
    echo "This dosent appear"
else
    fileNE="$name.$ext"
    touch ${fileNE}
    TemplateContent > ${fileNE}
    chmod 755 ${fileNE}
    if [[ ${PyWRKd} != ${PWD} ]] ; then
          mv ${fileNE} ${PyWRKd}/
    fi
    ln -s ${PyWRKd}/${fileNE} ${BinWRKd}/${fileNE}
    echo "Successfully created and enabled the file"
fi
}

enb

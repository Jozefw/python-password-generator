#!/bin/bash



python3 $1 $2

#exit code value
python_status=$?

current_date=`date "+%D %T"`

msg="A script has ran to completion:  

Server: $HOSTNAME
User: $USER

Script Name: $1 

Time: $current_date"

echo "$python_status"
echo "$msg"

msg="The following Script ran to error: $1 at $current_date"
if [ $python_status -eq 0 ]; then
    echo "$msg" | mailx -s "No Script Failure"  jozefcode@gmail.com;
fi;

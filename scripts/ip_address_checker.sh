#!/bin/bash

echo "Please enter the IP address seprated by space"

read -a ip_list

for i in ${ip_list[@]}
do 
    echo "################################"
    ping -c 1 -w 3 $i 2>&1 >/dev/null
    if [ $? -eq 0 ]
    then 
        echo "$i is up!"
    else 
        echo "$i is down"
    fi
done
#!/bin/bash
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
DATE=`date +%Y-%m-%d-%H-%M-%S`
OUTPUT="$(/usr/bin/iperf -c 35.185.100.110 -i 1 -t 10 -p 80)”
printf "%s" "$OUTPUT" >> bandwidth_test_$DATE.txt
echo "${OUTPUT}"

sudo iperf3 -c 35.185.100.110 -i 1 -t 10 -p 80
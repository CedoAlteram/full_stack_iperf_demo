#!/bin/bash
export NLS_LANG=AMERICAN_AMERICA.AL32UTF8
DATE=`date +%Y-%m-%d-%H-%M-%S`
OUTPUT="$(iperf3 -c 35.190.161.66 -i 1 -t 10 -p 80)"
printf "%s" "$OUTPUT" >> /var/www/FlaskApp/FlaskApp/static/bandwidth_test_$DATE.txt
echo "${OUTPUT}"

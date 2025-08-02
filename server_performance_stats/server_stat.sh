#!/bin/bash

echo "######################"
echo "# System Uptime Info #"
echo "######################"

uptime
echo


echo "# Total CPU Usage #"

top -bn1 | grep "%Cpu(s):" | cut -d ',' -f 4 | awk '{print "Usage: " 100-$1 "%"}'

echo


echo "# Total Memory Usage #"

free | grep "Mem:" -w | awk '{printf "MaxMem: %.1fGi\nUsedMem: %.1fGi (%.2f%%)\nFreeMem: %.1fGi (%.2f%%)\n",$2/1024^2, $3/1024^2, $3/$2 * 100, $4/1024^2, $4/$2 * 100}'

echo

echo "# Total Disk Usage #"

df -h | grep "/" -w | awk '{printf "Total: %sG\nUsed: %s (%.2f%%)\nFree: %s (%.2f%%)\n",$3 + $4, $3, $3/($3+$4) * 100, $4, $4/($3+$4) * 100}'

echo

echo "# Top 5 Processes by Memory Usage #"

ps aux --sort -%mem | head -n 6 | awk '{print $1 "\t" $2 "\t" $4 "\t" $4 "\t" $11}'

echo
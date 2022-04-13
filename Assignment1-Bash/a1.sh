#!bin/bash
while getopts h flag
do
    case "${flag}" in
        h)
        echo "1:Disk space"
        echo "2:Top 10 processes by CPU Usage"
        echo "3:Top 10 processes by RAM Usage"
        echo "4:All usages"
        ;;
    esac
done

getDiskSpace(){
    echo "-----Disk space-----"
    echo "$(df -H)"
}

getProcessesByCpu(){
    echo "-----Top 10 processes by CPU Usage-----"
    echo "$(ps -Ao pid,%cpu,comm --sort=-%cpu |head)"
}

getProcessesByMemory(){
    echo "-----Top 10 processes by RAM Usage-----"
    echo "$(ps -Ao pid,%mem,comm --sort=-%mem |head)"
}
echo "enter value :1/2/3/4"
read input
if [[ input -eq 1 ]]
then
    getDiskSpace

elif [[ input -eq 2 ]]
then
    getProcessesByCpu

elif [[ input -eq 3 ]]
then
    getProcessesByMemory
elif [[ input -eq 4 ]]
then
    getDiskSpace
    getProcessesByCpu
    getProcessesByMemory
else
    echo "Wrong option selected"
fi
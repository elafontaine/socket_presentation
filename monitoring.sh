#!/usr/bin/env bash
while [[ 1 ]];
    do sleep 1;
     clear;
     netstat -an| grep 15000;
     for pid in $(ps -ef| grep python| awk -F' ' '{print $2}');
        do echo $pid;
         ls -ltr /proc/$pid/fd;
     done;
done

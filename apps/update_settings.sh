#!/bin/bash 

APPS_DIR=/home/opendevops/apps

for x in $(find . -type d -maxdepth 1); do
 echo $x;
done
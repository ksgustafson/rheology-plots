#!/bin/bash

for file in *.txt
do
    python plotLogData.py $file 1
done

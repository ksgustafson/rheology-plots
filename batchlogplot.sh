#!/bin/bash

for file in *.txt
do
    python plotLogData.py --datafile $file --noshow
done

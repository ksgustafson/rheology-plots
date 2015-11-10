#!/bin/bash

for file in *.txt
do
    python plotData.py --datafile $file --noshow
done

#!/bin/bash

for file in *.txt
do
    python plotData.py $file 1
done

import argparse
import numpy
import copy
import matplotlib.pyplot as plt

# usage: plotData.py datafile [noshow]

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('--datafile')
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

data = open(args.datafile,'r')

l = args.datafile.split('.')
l.pop()
plotTitle = l[0]
l.append('.png')
l.insert(0,'plots/')
plotFile = ''.join(l)

for i in range(11):    # ignore experiment info at start of file
    data.readline()

numData = open(".temp","w")

for line in data:
    numData.write(line)

numData.close()
    
shear = list()
viscosity = list()

data = numpy.loadtxt(".temp", dtype=numpy.float64)

shear = data[:,4:5]
viscosity = data[:,5:6]

plt.plot(shear, viscosity)
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
plt.title(plotTitle)
plt.savefig(plotFile)
if not args.noshow:
    plt.show()


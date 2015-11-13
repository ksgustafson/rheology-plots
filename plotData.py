import argparse
import numpy
import matplotlib.pyplot as plt
import rheology

# usage: plotData.py --datafile datafile [--logplot] [--noshow]

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('--datafile')
parser.add_argument('--logplot', action='store_true')
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

shear, viscosity, plotFile, plotTitle = rheology.loadExperiment(args.datafile)

l = plotFile.split()
if args.logplot:
    l.insert(0,'logplots/')
else:
    l.insert(0,'plots/')
plotFile = ''.join(l)

if args.logplot:
    plt.loglog(shear, viscosity)
else:
    plt.plot(shear, viscosity)
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
plt.title(plotTitle)
plt.savefig(plotFile)
if not args.noshow:
    plt.show()


import argparse
import matplotlib.pyplot as plt
import numpy
import rheology

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('--datafiles', nargs='+')
parser.add_argument('--phi', nargs='+', type=float)
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

fileConcKeys = dict(zip(args.datafiles,args.phi))

avgViscosity = dict()

for phiVal in set(args.phi):
    fileGroup = list()

    for file in args.datafiles:
        if (fileConcKeys[file] == phiVal):
            fileGroup.append(file)

    avgViscosity[phiVal] = rheology.avgMeasurements(fileGroup)

phiList = list()
normViscosity = list()
for keys in avgViscosity:
    phiList.append(keys)
    normViscosity.append(avgViscosity[keys]/avgViscosity[0])

phirange = numpy.arange(0,0.05,0.001)
    
Einstein = list()
for val in phirange:
    Einstein.append(rheology.EinsteinPred(val))

BandG = list()
for val in phirange:
    BandG.append(rheology.BatchAndGreenPred(val))
    
plt.plot(phiList,normViscosity,'+',phirange,Einstein,phirange,BandG)
plt.xlabel('Particle Volume Fraction')
plt.ylabel('Relative Viscosity')
plt.legend(['Experimental','Einstein','Batchelor and Green'],loc='upper left')
plt.savefig('plots/EinsteinComparison.png')
if not args.noshow:
    plt.show()

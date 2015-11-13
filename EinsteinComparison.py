import argparse
import matplotlib.pyplot as plt
import numpy
import rheology

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('datafiles', nargs='+', type=file)
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

avgViscosity = list()

for data in args.datafiles:
    tmp1, viscosity, tmp2, tmp3 = rheology.loadExperiment(data)

    temp = 0
    for vals in viscosity[len(viscosity)-5:len(viscosity)]:
        temp = temp + vals
    avgViscosity.append(temp/5)
            
    data.close()

phi = [0, 0.005, 0.025, 0.05]
phiexpt = [0, 0.005, 0.025, 0.05]
#phiexpt = [0, 0.005, 0.005, 0.025, 0.025, 0.05, 0.05]

normViscosity = list()
for val in avgViscosity:
    normViscosity.append(val/avgViscosity[0])

Einstein = list()
for val in phi:
    Einstein.append(rheology.EinsteinPred(val))

BandG = list()
for val in phi:
    BandG.append(rheology.BatchAndGreenPred(val))
    
plt.plot(phiexpt,normViscosity,'+',phi,Einstein,phi,BandG)
plt.xlabel('Particle Volume Fraction')
plt.ylabel('Relative Viscosity')
plt.legend(['Experimental','Einstein','Batchelor and Green'],loc='upper left')
plt.savefig('plots/EinsteinComparison.png')
#plt.savefig('plots/EinsteinComparison2.png')
if not args.noshow:
    plt.show()

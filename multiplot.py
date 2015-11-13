import argparse
import matplotlib.pyplot as plt
import rheology

# usage: plotData.py datafile [noshow]

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('datafiles', nargs='+', type=file)
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

for data in args.datafiles:

    shear, viscosity, tmp1, tmp2 = rheology.loadExperiment(data)

    plt.plot(shear,viscosity)
    
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
if not args.noshow:
    plt.show()

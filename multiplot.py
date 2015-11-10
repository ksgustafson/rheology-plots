import argparse
import matplotlib.pyplot as plt

# usage: plotData.py datafile [noshow]

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('datafiles', nargs='+', type=file)
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

for data in args.datafiles:
    for i in range(11):    # ignore experiment info at start of file
        data.readline()

    shear = list()
    viscosity = list()

    for line in data:
        if line.split():
            templist = line.split()
            temp = templist.pop(4)
            shear.append(float(temp))
            temp = templist.pop(4)
            viscosity.append(float(temp))

    data.close()

    plt.plot(shear,viscosity)
    
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
if not args.noshow:
    plt.show()

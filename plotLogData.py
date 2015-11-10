import argparse
import matplotlib.pyplot as plt

# usage: plotLogData.py datafile [noshow]

parser = argparse.ArgumentParser(description='Process command line arguments')
parser.add_argument('--datafile')
parser.add_argument('--noshow', action='store_true')

args = parser.parse_args()

data = open(args.datafile,'r')

l = args.datafile.split('.')
l.pop()
plotTitle = l[0]
l.append('.png')
l.insert(0,'logplots/')
plotFile = ''.join(l)

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

plt.loglog(shear, viscosity)
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
plt.title(plotTitle)
plt.savefig(plotFile)
if not args.noshow:
    plt.show()

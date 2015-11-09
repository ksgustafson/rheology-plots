import sys
import matplotlib.pyplot as plt

datafile = sys.argv[1]

data = open(datafile,'r')

if len(sys.argv) >= 3:
    noshow = sys.argv[2]  # 1 if plots should not be shown
else:
    noshow = 0
    
if len(sys.argv) >= 4:
    plotFile = sys.argv[3]
else:
    l = datafile.split('.')
    l.pop()
    plotTitle = l[0]
    l.append('.png')
    l.insert(0,'plots/')
    plotFile = ''.join(l)

for i in range(11):
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

plt.plot(shear, viscosity)
plt.xlabel('Shear rate (1/s)')
plt.ylabel('Viscosity (Pa s)')
plt.title(plotTitle)
plt.savefig(plotFile)
if not noshow:
    plt.show()

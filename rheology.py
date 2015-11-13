import numpy

def loadExperiment(datafile):
    data = open(datafile,'r')

    l = datafile.split('.')
    l.pop()
    plotTitle = l[0]
    l.append('.png')
    plotFile = ''.join(l)

    for i in range(11):    # ignore experiment info at start of file
        data.readline()

    numData = open(".temp","w")

    for line in data:
        numData.write(line)

    data.close()
    numData.close()
    
    data = numpy.loadtxt(".temp", dtype=numpy.float64)

    shear = data[:,4:5]
    viscosity = data[:,5:6]

    return shear, viscosity, plotFile, plotTitle

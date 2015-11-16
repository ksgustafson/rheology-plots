import numpy

def loadExperiment(datafile,labels):  # labels should be one if labels
    data = open(datafile,'r')         # should be returned

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

    if labels:
        return shear, viscosity, plotFile, plotTitle
    else:
        return shear, viscosity

def avgMeasurements(expts):
    avgViscosity = 0
    varViscosity = 0
    numExpts = 0
    for file in expts:
        shear, viscosity = loadExperiment(file,0)

        temp = 0
        for vals in viscosity[len(viscosity)-5:len(viscosity)]:
            temp = temp + vals

        varViscosity = varViscosity + temp*temp/25
        avgViscosity = avgViscosity + temp/5
        numExpts = numExpts + 1

    avgViscosity = avgViscosity/numExpts
    varViscosity = varViscosity/numExpts - avgViscosity*avgViscosity

    errViscosity = numpy.sqrt(varViscosity/numExpts)
    
    return avgViscosity, errViscosity

def EinsteinPred(phi):
    return (1 + 2.5*phi)

def BatchAndGreenPred(phi):
    return (EinsteinPred(phi) + 7.6*phi*phi)

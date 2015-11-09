# rheology-plots

plotData.py and plotLogData.py are python scripts which accept up to three arguments with the following syntax

plotData.py datafiletoload.txt 0 [plotfilename]

the first argument gives the name of the file to load shear stress and viscosity data from
second argument is boolean for not showing plots (1 means do not show plots, just save them to the file name)
third argument is to specify a name for the plot file, currently if this argument is used the "no show" argument must also be included

default behavior with only one argument is to plot the data from that file, show the plot, and save the plot to folder plot (or logplot for plotLogData.py) in the same directory as the data file

the shell scripts are used to plot all data files in the current directory without showing any plots, just saving them as files
# rheology-plots

plotData.py and plotLogData.py are python scripts which accept up to three arguments with the following syntax

plotData.py --datafile datafiletoload.txt [--noshow]

the first argument gives the name of the file to load shear stress and viscosity data from
second argument specifies not to show the plot

default behavior with only one argument is to plot the data from that file, show the plot, and save the plot to folder plot (or logplot for plotLogData.py) in the same directory as the data file

the shell scripts are used to plot all data files in the current directory without showing any plots, just saving them as files

multiplot.py is called as

multiplot.py file1 [file2 file3 ...] [--noshow]

where the data from file1, file2, etc will be plotted on the same figure
as of now, multiplot should be called from the command line as

python -i multiplot.py file1 ... --noshow

so that the legend can be added before saving

as an example, to be called after entering the interpreter,

plt.legend(['0 percent','0.5 percent','2.5 percent','5.0 percent'],bbox_to_anchor=(0.5, 1.1), loc='upper center', ncol=2)
plt.savefig('filename')

which will make a two column legend at the top of the figure, overlapping the top border slightly

Plan to convert scripts for loading shear and viscosity data from a file to streamline all code, can have these as functions which return numpy arrays of shear values, viscosity values
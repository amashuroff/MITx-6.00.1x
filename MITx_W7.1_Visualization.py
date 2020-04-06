"""
Using Pylab
Pylab provides access to existing set of graphing/plotting procedures
Remember to call figure (display) before making changes to the plot
"""
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)


plt.figure("exp")                        # creating a new display for our plot, naming it
plt.xlabel("sample points")
plt.ylabel("exponential function")       # creating labels for our plot
plt.title("Exponential")                 # creating title
plt.ylim(0,1000)                         # setting a limit on a y axis (comparing plots with different scaling)
plt.plot(mySamples, myExponential)       # lists need to be of the same length
plt.show()

plt.figure('quad')
plt.plot(mySamples, myQuadratic)
plt.show()

# remember to clean the window (display), before redrawing it,
# because we are reusing a previously created display window
plt.figure("lin")
plt.clf()

# creating an overlaying plot
plt.figure("exp cub")
plt.clf()
plt.plot(mySamples, myExponential, label = 'exponential')       # adding labels and legend for functions
plt.plot(mySamples, myCubic, label = 'cubic')
plt.legend(loc = 'upper left')                      # if called plt.legend() - pylab will decide where to put legend
plt.ylim(0, 1000)
plt.show()

# comparing functions, controlling display parameters
plt.figure('lin quad')
plt.clf()
plt.subplot(211)                   # args are, rows, columns, which location to use
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)         # first letter = color
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)   # second char = variation of the line (- -- ^ o)
plt.show()

# if you have something that grows really rapidly, can use log scale, plt.yscale('log')

import sympy
import numpy as np
import math
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def coordfinder(infile,outfile):
    ''' Based on a set of calculated coordinates, assign a normal distribution function to each coordinate, sum those functions and plot a probability density distribution of coordinate location for each axis'''
    A, B, X, Y = sympy.symbols("a,b,x,y")
    eq = sympy.Eq(Y, ((1/(A*sympy.sqrt(2*sympy.pi)))*sympy.exp(-0.5*((X-B)/A)**2)))
    eqy = sympy.solve(eq,Y)[0]
    df = pd.read_csv(infile)

    for m in ["x","y","z"]:
        print(m)
        data = df[m]
        summed_normal_distribution_function = 0
        count = 0

        #for i in data.index:
        for i in data.sample(n=100).index:
            count += 1
            normal_distribution_function = eqy.subs({A:2, B:data[i]})
            function = sympy.lambdify((X), normal_distribution_function)
            summed_normal_distribution_function += normal_distribution_function

        function = sympy.lambdify((X),summed_normal_distribution_function)
        x2 = np.linspace(-30, 50, 1000)
        y2 = function(x2)/count
        plt.plot(x2, y2, label=m)

    plt.xlabel("Model coordinate")
    plt.ylabel("Estimated PRE location")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    infile = "cleandf.csv"
    coordfinder(infile,outfile) 

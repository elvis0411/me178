from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from scipy.integrate import quad

##
def f(x_1,x_2):
    return x_1**3/3-4*x_1+x_2**3/3-16*x_2

def q2():
    x_1 = x_2 = np.linspace(-1000,1000, num = 10000) 

    X1, X2 =  np.meshgrid(x_1,x_2)

    y = f(X1,X2)


    #fig = plt.figure()
    #ax = plt.axes(projection = '3d')
    #
    #ax.contour3D(X1, X2, y, 100, cmap='binary')
    ##ax.view_init(60, 35)
    ##fig
    #plt.show()

    x1 = [2,-2]
    x2 = [4,-4]
    ans = [f(i,j) for i in x1 for j in x2 ]

    print(max(ans))

def q3():
    
    def eq(t):
        return t*0.1*np.exp(-0.1*t)
    
    result = quad(eq,0,np.inf)
    print(result)

q3()
    

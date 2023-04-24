# %% [markdown]
# # Trigonometrical method #
# Tasks:
# 1. numerical analysis of mechanism
# 2. optimization of mechanism
# 3. control of mechanism
# ## Python Intro ##
# Why Python -> it is free!
# - libraries
# - variables, numbers, lists ...
# - flow control
# - function definition
# - plotting

# %% [markdown]
# ### Libraries ###
# - use the available useful functions
# - the functions are gather in the libraries
# - the libraries are usually open-source projects
# - you can download them directly (from Git etc.) or using pip (https://pypi.org/project/pip/)

# %%
# The Python Standard Libraries                 https://docs.python.org/3/library/index.html
# - standard built-in, without installation 
import math

# Basic library for numerical calculation       https://numpy.org/doc/stable/user/quickstart.html
# - Numpy vs. Matlab                            https://numpy.org/doc/stable/user/numpy-for-matlab-users.html
import numpy

# Basic library for plotting                    https://matplotlib.org/
from matplotlib import pyplot as plt

# %% [markdown]
# ### Variables, Numbers, Lists ... ###
# - you can easily define neccesary variables
# - the variables are usually defined without data type definition (boolean, int, string ... ) - all types are objects

# %%
a = 0.1 # [m]
b = 0.5 # [m]
c = 0.3 # [m]

angle_fi_0_s = 0 # [rad]
angle_fi_0_e = 2*math.pi # [rad], pi is defined in the library math as constant
angle_fi_0_num_division = 1000 # number of sections between the angle_fi_0 and the angle_fi_1

# using function from the imported library numpy 
# each function has specified parameters
angles_fi_0 = numpy.linspace(angle_fi_0_s, angle_fi_0_e, angle_fi_0_num_division) # get list of angles between the angle_fi_0 and the angle_fi_1

# basic printing function - print()
# parameter can be a functional string - f'' 
print(f'List of angles: {angles_fi_0} rad')

# %% [markdown]
# ### Programme flow control ###
# - the standard flow control tools are defined in Python https://docs.python.org/3/tutorial/controlflow.html
# - programme blocks are defined by indentation

# %%
# empty list of coordinates defition
x_B = []
y_B = []

for phi_1 in angles_fi_0:
    # calculate defined values
    dis_AS2 = math.sqrt((a*math.cos(phi_1)-c)**2 + (a * math.sin(phi_1))**2)
    dis_BS2 = b - dis_AS2
    phi_2 = math.atan(a * math.sin(phi_1) / (c - a * math.cos(phi_1)))

    # append new values to existing lists
    x_B.append(dis_BS2 * math.cos(-phi_2) + c)
    y_B.append(dis_BS2 * math.sin(-phi_2))


# %% [markdown]
# ### Function definition and Plotting ###
# - you can easily define own functions -> do it!
# - decompose your code into function blocks
# - add description of your function into the code
# - describe inputs and outputs of the function

# %%
def make_2D_graph(x, y, x_name, y_name, title):
    """
    Funtion plots the data [x, y] into 2D graph.

    param x: x data
    type  x: int
    param y: y data
    type  y: int
    param x_name: name of the x axis
    param x_name: str
    param y_name: name of the y axis
    param y_name: str
    param title: title of the graph
    param title: str
    """
    plt.figure(dpi=100)
    ax = plt.axes()
    ax.set_xlabel(x_name, labelpad=20)
    ax.set_ylabel(y_name, labelpad=20)
    ax.set_title(title)
    # plot line - parameters https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
    ax.plot(x, y, 'r', linewidth=1)
    ax.grid(True)

# example of usage the defined function
# plot the trajectory of point B[x_B, y_B]
make_2D_graph(x_B, y_B, 'x [m]', 'y [m]', 'Trajectory of point B')



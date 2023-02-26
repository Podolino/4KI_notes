# %% [markdown]
# # Ex. 2 - Motion of point
# 
# ## Analytical solution
# 
# We have calculated the analytical solution using second-order differential equations. We have obtained the results - two functions $v_x = f(t)$ and $x = f(t)$.
# 
# $v_x = -\frac{1}{4}\cdot t^2 + 10\cdot t$
# 
# $x = -\frac{1}{12}\cdot t^3 + 5\cdot t^2$

# %%
import numpy as np

num_points = 10000 # number of points in the defined time range [0, 20] s

t_ana = np.linspace(0, 20, num_points)

# calculation of the analytical solution
v_ana = -1/4 * t_ana**2 + 10 * t_ana
x_ana = -1/12 * t_ana**3 + 5 * t_ana**2

# %% [markdown]
# ## Numerical solution - Explicit Euler method
# 
# We have simply derived the approximate explicit Euler numerical solution from the analytical one. The method is based on the linear approximation of the function using the first-order Taylor polynomial:
# 
# $y(x + h) \approx y(x_0) + \dot{y}(x_0) \cdot h$

# %%
steps = 100 # number of steps in the time range [0, 20] s using for the numerical solution
# initial conditions
t0 = 0 # [s]
x0 = 0 # [m]
v0 = 0 # [m/s]

t_finish = 20 # [s]
delta_t = t_finish/steps # [s], time step of numerical solution 

# initial assignment
v_k_1 = v0
x_k_1 = x0

# logs
x_num = []
v_num = []
t_num = []

# do defined steps + 1
for k in range(steps + 1):
    t_k = t0 + k*delta_t
    a_k = -1/2 * t_k + 10

    # calculation of k-step using Taylor polynom (the first derivation of v and x)
    v_k = v_k_1 + a_k * delta_t
    x_k = x_k_1 + v_k * delta_t

    # assignment for the next step
    v_k_1 = v_k
    x_k_1 = x_k

    # logs
    print(f"Step:{k}, Time:{t_k:.2f} s, x={x_k_1:.2f} m, v={v_k_1:.2f} m/s")

    t_num.append(t_k)
    v_num.append(v_k_1)
    x_num.append(x_k_1)

# %% [markdown]
# ## Plot results
# We can compare both obtained results. 

# %%
import matplotlib.pyplot as plt
# plot x_ana and x_num as f(t)
plt.plot(t_num, x_num, 'r')
plt.plot(t_ana, x_ana, 'b')
plt.legend(['Numerical (approximate)', 'Analytical (exact)'])
plt.xlabel('t [s]')
plt.ylabel('x [m]')
plt.grid(True)
plt.title('x = f(t)')
plt.show()

# plot the error of result
print(f"Analytical result: x_ana(t = 20s) = {x_ana[-1]:.2f} m")
print(f"Numerical result: x_num(t = 20s) = {x_num[-1]:.2f} m")
print(f"Error:  |x_num(t = 20s) - x_ana(t = 20s)| = |{abs(x_num[-1] - x_ana[-1]):.2f}| m")



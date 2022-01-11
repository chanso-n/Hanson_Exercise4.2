# import libraries
import math
import sympy as sp

# assign x for (e)
x = sp.Symbol('x')

# calculating limits numerically
# (a)
# assign x values
fx1 = 2
fx2 = 2.5
fx3 = 2.75
fx4 = 2.9
fx5 = 2.99
fx6 = 2.999
fx7 = 2.9999

# evaluating function f with assigned values
fy1 = 2*fx1**3 - 4*fx1 + 1
fy2 = 2*fx2**3 - 4*fx2 + 1
fy3 = 2*fx3**3 - 4*fx3 + 1
fy4 = 2*fx4**3 - 4*fx4 + 1
fy5 = 2*fx5**3 - 4*fx5 + 1
fy6 = 2*fx6**3 - 4*fx6 + 1
fy7 = 2*fx7**3 - 4*fx7 + 1

print(fy1, fy2, fy3, fy4, fy5, fy6, fy7)
# (a) Answer:  9, 22.25, 31.59375, 38.178, 42.50179800000001, 42.95001799800001, 42.99500017999799
# the limit as x approaches 3 is 43 


# (b)
# assign x values
e = math.e
gx1 = .2
gx2 = .1
gx3 = .01
gx4 = .001
gx5 = .0001

# evaluating function g with assigned values
gy1 = (e**gx1 - 1) / gx1
gy2 = (e**gx2 - 1) / gx2
gy3 = (e**gx3 - 1) / gx3
gy4 = (e**gx4 - 1) / gx4
gy5 = (e**gx5 - 1) / gx5

print(gy1, gy2, gy3, gy4, gy5)
# (b) Answer: 1.1070137908008493, 1.0517091807564771, 1.005016708416795, 1.0005001667083846, 1.000050001667141
# the limit as x approaches 0 is 1

# (c) Answer: For part a, yes. F(3) = 43, which aligns with the generated values as we used numbers closer and
# closer to the limit of 3. For part b, no. Since 0 cannot be in the denominator of a fraction, inputting 0
# returns an error. This means that when plotted, a returns a continuous line, while b returns a line with a gap
# where x = 0. 



# average rate of change
# define mathematical function (also a python function)
def for_arc(x):
    return 3*x**2

# define function that takes in a mathematical function and two numbers a and b
def arc(func, a, b):
    return (func(b) - func(a)) / (b - a)

#print(arc(for_arc, 3, 5))


# average rate of change to instantaneous rate of change
# (a)
# define a function for questions a-e
def dist_meters(t):
    return 4.9*t**2

print('a.', arc(dist_meters, 5, 6))
# (a) Answer: 53.89999999999999

# (b)
print('b.', arc(dist_meters, 5, 5.5))
# (b) Answer: 51.45000000000002

# (c)
print('c.', arc(dist_meters, 5, 5.1))
# (c) Answer: 49.490000000000016

# (d)
print('d.', arc(dist_meters, 4.9, 5))
print('d.', arc(dist_meters, 4.9, 5.1))
# (d) Answer: 49

# (e)
# this method uses the sympy library
print(sp.diff(4.9*(x**2)))
# this method returns 9.8*x

# or I could find the derivative by hand and build a python function
def der(t):
    return 2*4.9*t

# (f)
print('f.', der(5))
# (f) Answer: 49.0. In (d) I found the limit of the average rate of change of f(t) as t approaches 5. This
# returned the same value as f'(t) when t = 5 because the derivative of a function returns the instantaneous
# rate of change at any given point. 



# calculating and interpreting partial derivatives
# (a)
# build a function to evaluate the given values
def pred(c, y):
    return 16000 + 2400*c - 1800*y

print('predicted selling price:', pred(8, 5))
# (a) Answer: The predicted selling price would be $26,200

# (b) the partial derivative is 2,400. Current condition of the vehicle strongly increases the predicted selling
# price

# (c) the partial derivative is -1,800. Age of the car in years moderately decreases the predicted selling price




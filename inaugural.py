from types import SimpleNamespace
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

def utility(z): #Generates a utility function taking the variable z.
    return (z**(1+par.theta))/(1+par.theta)

def premium(q): #Generates a function for caltulating the premium denoted pi.
    return par.p*q

def exp_value(i,q): 
    z1 = par.y-i+q-premium(q,p)
    z2 = par.y-premium(q,p)
    return par.p*utility(z1)+(1-par.p)*utility(z2)

def opt_q(i):
    from scipy import optimize
    obj = lambda q: -exp_value(i,q)
    solution = optimize.minimize_scalar(obj,bounds=(0,0.9),method='bounded') #Bounded
    q = solution.x
    return q

def exp_value2(q,premium):
    return 0.2*utility(1.0-0.6+q-premium) + (1-0.2)*utility(1.0-premium)

def acceptable(q,premium):
    return exp_value2(q,premium)-exp_value2(0,0)

def average_eq(gamma,premium):
    z1 = par.y-(1-gamma)*x-premium
    z2 = par.y-premium
    return np.mean(par.p*utility(z1)+(1-par.p)*utility(z2))

def diff(premium):
    z1 = par.y(1-0.95)*x-premium
    z2 = par.y-premium
    return np.mean(par.p*utility(z1)+(1-par.p)*utility(z2)-utility(par.y-x))
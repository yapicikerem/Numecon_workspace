from types import SimpleNamespace
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from scipy.stats import beta

par = SimpleNamespace(y = 1, p = 0.2, theta = -2, g = 0.95, x = 0.6, a = 2, b = 7, N = 100000)

def utility(z,par):
    """
    Generates a utility function taking the variable z.
    
    z: Defines the function that needs to be evaluated.
    theta: Parameter in the utility function gobally takes the value '-2'.
    """
    return (z**(1+par.theta))/(1+par.theta)

def premium(q,par): 
    """
    Generates a function for caltulating the premium denoted pi.
    
    p: Parametervalues that defines the probability of either actions taken.
    q: Denotes the coverage amount.
    """
    return par.p*q

def exp_value(x,q,par): 
    """
    This function generates the expected value dependant on the utility and
parameters from earlier.
    
    x: The monetary loss.
    q: Denotes coverage amount.
    z1: Defines the part of the valuefunction that comes from the situation where an incident occurs.
    z2: Defines the other part of the valuefunction where an incident does not occur.
    """
    
    z1 = par.y-x+q-premium(q,par)
    z2 = par.y-premium(q,par)
    return par.p*utility(z1,par)+(1-par.p)*utility(z2,par)

def optimal_q(x):
    """
    This function generates the optimal q-value by optimizing the negative expected value function. The call of this function returns the optimal q-value.
    
    x: The monetary loss.
    """
    from scipy import optimize
    obj = lambda q: -exp_value(x,q,par)
    solution = optimize.minimize_scalar(obj,bounds=(0,0.9),method='bounded')
    q = solution.x
    return q

def exp_value_pi(q,premium,par):
    """
    This function generates the expected value with the premise of finding the optimal premium.
    
    q: Denotes the coverage amount.
    premium: Denotes the coverage premium.
    """
    return par.p*utility(par.y-par.x+q-premium,par) + (1-par.p)*utility(par.y-premium,par)

def acceptable(q,premium):
    """
    This function denotes the acceptable contracts since it takes the difference og the expected value functions.
    
    q: Denotes the coverage amount.
    premium: Denotes the coverage premium.
    """
    return exp_value_pi(q,premium,par)-exp_value_pi(0,0,par)

def average_eq(gamma,premium,par):
    """
    This function generates generates the expected value with gamma as a variable.
    
    gamma: Defines the coverage ratio.
    premium: Denotes the coverage premium.
    z1: Defines the part of the valuefunction that comes from the situation where an incident occurs.
    z2: Defines the other part of the valuefunction where an incident does not occur.
    """
    z1 = par.y-(1-gamma)*x-premium
    z2 = par.y-premium
    return np.mean(par.p*utility(z1,par)+(1-par.p)*utility(z2,par))

def difference(premium,par):
    """
    This function generates the expected value with the addition of the a being drawn from a beta-distribution.
    
    premium: Denotes the coverage premium.
    x: generated from a beta-distribution.
    z1: Defines the part of the valuefunction that comes from the situation where an incident occurs.
    z2: Defines the other part of the valuefunction where an incident does not occur.
    """
    from scipy.stats import beta
    x = beta.rvs(par.a, par.b, size=par.N)
    z1 = par.y-(1-par.g)*x-premium
    z2 = par.y-premium
    np.seterr(invalid='ignore') #Used to avoid irelevant erros like zreo divide error.
    return np.mean(par.p*utility(z1,par)+(1-par.p)*utility(z2,par)-utility(par.y-x,par))
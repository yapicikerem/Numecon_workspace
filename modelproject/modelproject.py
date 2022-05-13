
#Imports 
from numpy import array #importing array

#Defining demand and cost function
def demand_good_x(x_i,x_j):
    """
    This function decides the demand given the quantity produced by firms i and j. This means that this function decides
    the price of the good. This works because the goods are homogenous and operate under the same market.
    
    x_i (float): The good produced by firm i
    x_j (float): The good produced by firm j
    120: This constant defines the quantity for which demand and thereby the price is equal to zero
    """
    return 120-(x_i+x_j)

def cost_good_x(x):
    """
    This is the cost function that defines the production costs of good x given the amount produced. 
    The function is of such form that is only catches variable cost, and that there therefore is no fixed costs.
    
    x(float): the quantity of good x
    30: Predetermined constant
    """
    return 30*x

#Defining profits function for firm i and firm j
def profit(x_i,x_j):
    """
    This profit function is of the original form and is used to find the optimal production.
    
    x_i (float): The good produced by firm i
    x_j (float): The good produced by firm j
    """
    return demand_good_x(x_i,x_j)*x_i-cost_good_x(x_i)

#Defining reaction function 
def best_response(x_j):
    """
    This function is derived from the profit function by taking the derevation with regards to x_i and isolating x_i.
    
    x_i (float): The good produced by firm i
    x_j (float): The good produced by firm j
    """
    x_i = (90-x_j)/2
    return x_i

def vector_best_response(x):
    """
    Now we take the best response functions and generating a vector containing them this is then used to solve the system
    of functions that are driven from earlier functions. Because we are looking for the vector best responce, we minus the
    response functions from an x.
    
    x (float): creating the difference equation that is optimized.
    """
    return array(x)-array([best_response(x[1]),best_response(x[0])])

#Extension 1 - Collusion
def negative_profit_collusion(x): #Negative, because the minimizer underneath needs the negative value to find maximum.
    return -(90*x-2*x**2)
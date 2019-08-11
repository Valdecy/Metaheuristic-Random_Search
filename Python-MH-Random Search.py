############################################################################

# Created by: Prof. Valdecy Pereira, D.Sc.
# UFF - Universidade Federal Fluminense (Brazil)
# email:  valdecy.pereira@gmail.com
# Course: Metaheuristics
# Lesson: Random Search

# Citation: 
# PEREIRA, V. (2018). Project: Metaheuristic-Random_Search, File: Python-MH-Random Search.py, GitHub repository: <https://github.com/Valdecy/Metaheuristic-Random_Search>

############################################################################

# Required Libraries
import numpy  as np
import math
import random
import os

# Function
def target_function():
    return

# Function: Initialize Variables
def initial_position(solutions = 3, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    position = np.zeros((solutions, len(min_values) + 1))
    for i in range(0, solutions):
        for j in range(0, len(min_values)):
             position[i,j] = random.uniform(min_values[j], max_values[j])
        position[i,-1] = target_function(position[i,0:position.shape[1]-1])
    return position

# Function: Updtade Position
def update_position(position, min_values = [-5,-5], max_values = [5,5], target_function = target_function):
    updated_position = np.copy(position)
    for i in range(0, updated_position.shape[0]):
        for j in range(0, len(min_values)):
             rand = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
             updated_position[i,j] = np.clip(min_values[j] + (max_values[j] - min_values[j])*rand, min_values[j], max_values[j])               
        updated_position[i,-1] = target_function(updated_position[i,0:updated_position.shape[1]-1])            
    return updated_position

# RS Function
def random_search(solutions = 5, min_values = [-5,-5], max_values = [5,5], iterations = 50, target_function = target_function):    
    count = 0
    position = initial_position(solutions = solutions, min_values = min_values, max_values = max_values, target_function = target_function)
    best_solution = np.copy(position[position [:,-1].argsort()][0,:])
    while (count <= iterations):  
        print("Iteration = ", count, " f(x) = ", best_solution[-1])        
        position = update_position(position, min_values = min_values, max_values = max_values, target_function = target_function)
        if(best_solution[-1] > position[position [:,-1].argsort()][0,:][-1]):
            best_solution = np.copy(position[position [:,-1].argsort()][0,:])      
        count = count + 1  
    print(best_solution)    
    return best_solution

######################## Part 1 - Usage ####################################

# Function to be Minimized (Six Hump Camel Back). Solution ->  f(x1, x2) = -1.0316; x1 = 0.0898, x2 = -0.7126 or x1 = -0.0898, x2 = 0.7126
def six_hump_camel_back(variables_values = [0, 0]):
    func_value = 4*variables_values[0]**2 - 2.1*variables_values[0]**4 + (1/3)*variables_values[0]**6 + variables_values[0]*variables_values[1] - 4*variables_values[1]**2 + 4*variables_values[1]**4
    return func_value

rs = random_search(solutions = 75, min_values = [-5,-5], max_values = [5,5], iterations = 1000, target_function = six_hump_camel_back)

# Function to be Minimized (Rosenbrocks Valley). Solution ->  f(x) = 0; xi = 1
def rosenbrocks_valley(variables_values = [0,0]):
    func_value = 0
    last_x = variables_values[0]
    for i in range(1, len(variables_values)):
        func_value = func_value + (100 * math.pow((variables_values[i] - math.pow(last_x, 2)), 2)) + math.pow(1 - last_x, 2)
    return func_value

rs = random_search(solutions = 100, min_values = [-5,-5], max_values = [5,5], iterations = 5000, target_function = rosenbrocks_valley)

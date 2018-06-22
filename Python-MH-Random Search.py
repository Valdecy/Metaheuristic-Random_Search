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
import pandas as pd
import numpy  as np
import math
import random
import os

# Function: Initialize Variables
def initial_position(solutions = 5, min_values = [-5,-5], max_values = [5,5]):
    position = pd.DataFrame(np.zeros((solutions, len(min_values))))
    position['Fitness'] = 0.0
    for i in range(0, solutions):
        for j in range(0, len(min_values)):
             position.iloc[i,j] = random.uniform(min_values[j], max_values[j])
        position.iloc[i,-1] = target_function(position.iloc[i,0:position.shape[1]-1])
    return position

# Function: Updtade Position
def update_position(position, min_values = [-5,-5], max_values = [5,5]):
    updated_position = position.copy(deep = True)
    for i in range(0, updated_position.shape[0]):
        for j in range(0, len(min_values)):
             rand = int.from_bytes(os.urandom(8), byteorder = "big") / ((1 << 64) - 1)
             updated_position.iloc[i,j] = min_values[j] + (max_values[j] - min_values[j])*rand
             if (updated_position.iloc[i,j] > max_values[j]):
                updated_position.iloc[i,j] = max_values[j]
             elif (updated_position.iloc[i,j] < min_values[j]):
                updated_position.iloc[i,j] = min_values[j]                
        updated_position.iloc[i,-1] = target_function(updated_position.iloc[i,0:updated_position.shape[1]-1])            
    return updated_position

# RS Function
def random_search(solutions = 5, min_values = [-5,-5], max_values = [5,5], iterations = 50):    
    count = 0
    position = initial_position(solutions = solutions, min_values = min_values, max_values = max_values)
    best_solution = position.iloc[position['Fitness'].idxmin(),:]

    while (count <= iterations):
        
        print("Iteration = ", count, " f(x) = ", best_solution[-1])
               
        position = update_position(position, min_values = min_values, max_values = max_values)
        if(position.iloc[position['Fitness'].idxmin(),-1] < best_solution[-1] ):
            for j in range(0, position.shape[1]):
                best_solution[j] = position.iloc[position['Fitness'].idxmin(),j]
        
        
        count = count + 1 
        
    print(position.iloc[position['Fitness'].idxmin(),:].copy(deep = True))    
    return position.iloc[position['Fitness'].idxmin(),:].copy(deep = True)

######################## Part 1 - Usage ####################################

# Function to be Minimized. Solution ->  f(x1, x2) = -1.0316; x1 = 0.0898, x2 = -0.7126 or x1 = -0.0898, x2 = 0.7126
def target_function (variables_values = [0, 0]):
    func_value = 4*variables_values[0]**2 - 2.1*variables_values[0]**4 + (1/3)*variables_values[0]**6 + variables_values[0]*variables_values[1] - 4*variables_values[1]**2 + 4*variables_values[1]**4
    return func_value

rs = random_search(solutions = 25, min_values = [-5,-5], max_values = [5,5], iterations = 5000)

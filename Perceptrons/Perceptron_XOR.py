import numpy as np
#Implementing a XOR Perceptron function, with treshold -2 in second step and 1.5 in first step
def perceptron(inputs,weights,treshold):
    result_first_step = Unit_Function(inputs,weights,treshold)
    
    treshold = 0.5
    new_weight = -2

    inputs.append(result_first_step)
    weights.append(new_weight);
    
    result_second_step = Unit_Function(inputs,weights,treshold)
    result_perceptron = result_second_step
    
    return result_perceptron

def threshold_function(input,treshold):
    if (input >= treshold):
        result = 1
    else:
        result = 0
        
    return result

def Unit_Function(inputs,weights,treshold):
    # weighted multiply
    summarray = np.multiply(inputs,weights)
    summarray = np.sum(summarray)
    
    result_threshold = threshold_function(summarray,treshold)
    
    return result_threshold

print("How many entries do you have? ? \n")
N = int(input("Number of input values ​​x: "))
inputs = [0]*N
weights = [0]*N
treshold = 1.5


for i in range(len(inputs)):
    x = int(input("Value"+str(i)+" input: "))
    inputs[i]=x

print("----------------------------")

for i in range(len(weights)):
    x = int(input("Weight"+str(i)+" input: "))
    weights[i]=x

print("----------------------------")

result = perceptron(inputs,weights,treshold)
print("Logical NAND with perceptron: " + str(result))


import numpy as np
#Implementing a NAND Perceptron function
def perceptron(inputs,weights,treshold):
    result_and = And_Function(inputs,weights,treshold)
    result_perceptron = NOT_Function(result_and)
    
    return result_perceptron

def threshold_function(input,treshold):
    if (input >= treshold):
        result = 1
    else:
        result = 0
    
def NOT_Function(result_and):
    if (result_and == 1):
        result_not = 0
    else: 
        result_not = 1
    return result_not

def And_Function(inputs,weights,treshold):
    # weighted multiply
    summarray = np.sum(np.multiply(inputs,weights))
    # and function
    result_and = threshold_function(summarray,treshold)
    return result_and

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


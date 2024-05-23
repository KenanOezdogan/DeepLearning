import numpy as np

def perzeptron(inputs,weights,treshold):
    summ = Sum_function(inputs,weights)
    result = treshold_function(summ,treshold)
    
    return result
    
def treshold_function(summ,treshold):
    if (summ >= treshold):
        result = 1
    else: 
        result = 0
    return result

def Sum_function(inputs,weights):
    summarray = np.multiply(inputs,weights)
    summ = np.sum(summarray)
    return summ

print("How many entries do you have? \n")
N = int(input("Number of input values ​​x: "))
inputs = [0]*N
weights = [0]*N
treshold = 1

for i in range(len(inputs)):
    x = int(input("Value"+str(i)+" input: "))
    inputs[i]=x

print("----------------------------")


for i in range(len(weights)):
    x = int(input("Weight"+str(i)+" input: "))
    weights[i]=x

print("----------------------------")

result = perzeptron(inputs,weights,treshold)
print("Logical OR with perceptron: " + str(result))


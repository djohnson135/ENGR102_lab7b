
"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”

Name : Dathan Johnson
Section : 409
Assignment : lab 7b - 2
Date : 2-28-19
"""
#define variables
import math
sumA = 0
AB_add = 0
#empty lists
addlist = []
AB_subtract = 0
sublist = []
sumB = 0
dotproduct = 0
vectorA = []
vectorB = []
#input for dimensin
dimension = int(input('dimension: '))
#range of the dimension to find vector values
#assign vector to list
for i in range(dimension):
    vA = float(input('Vector A value: '))
    vB = float(input('Vector B value: '))
    vectorA.append(vA)
    vectorB.append(vB)
    AB_add = vectorA[i] + vectorB[i] #add vectors
    addlist.append(AB_add)
    AB_subtract = vectorA[i] - vectorB[i] #subtract vectors
    sublist.append(AB_subtract)
    dotproduct += vectorA[i] * vectorB[i] #find dotproduct
    sumA += vectorA[i] ** 2
    magA = abs(math.sqrt(sumA)) #find magnitude of vectors
    sumB += vectorB[i] ** 2
    magB = abs(math.sqrt(sumB))
#print statements
print('Magnitude of A: ',magA)
print('Magnitude of B: ',magB)
print('A + B: ', addlist)
print('A - B: ', sublist)
print('Dot product of A and B: ', dotproduct)



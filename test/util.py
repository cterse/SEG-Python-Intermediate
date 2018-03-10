'''
Created on 13-Feb-2018

@author: DELL
'''
def displayMatrix(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(str(a[i][j]) + " ", end="")
        print("\n")

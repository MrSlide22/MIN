# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:37:24 2016

@author: slide22
"""

import random

nusers = 5
nitems = 15
regions = 3
percentages = [1, 0.3, 0.1]

table = []

#Genera una lista con tantos 1s con el porcentaje de 1s dado
#el resto vale 0
def ponderatedList(perc):
    ret = [0 for x in range(100)]
    j = perc * 100
    for i in range(int(j)):
        ret[i] = 1
    return ret

#Devuelve un 1 si el usuario ha comprado el elemento
def setPurchased(i, j):
    region = j / (nitems / regions)
    percentage = (region + i) % regions
    l = ponderatedList(percentages[percentage])
    return  l[random.randint(0, 99)]

for i in range(nusers):    
    table.append([])
    for j in range(nitems):
        table[i].append(setPurchased(i, j)); # I want more probabilities of 0 than 1
        
def printTable():
    
    for i in range(nusers):
        row = ''
        for j in range(nitems):
             row += str(table[i][j])
        print row
        
def whoPurchasedItem(item):
    customers = []
    
    for i in range(nusers):
        if table[i][item] == 1:
            customers.append(i)
            
    return customers

def similarity(user):

    # uncomment when is fixed and substitute 0 in whoPurcha... by item    
    # iterate all products
    # for item in range(nitems):
        
    customers = whoPurchasedItem(0) # foreach item we get who purchased it
    items = dict() # auxiliar variable
    print "Users who bought item 0: " + str(customers)
    
    for c in customers: # now, we want to know the other items the customers had bought
                        # and store them into items
        for i in range(nitems):
            
            if table[c][i] == 1 and i != 0:
                items[i] = 1
    
    #just print some info
    p = "Other items bought by customers: "
    for key in items:
        p += str(key) + ", "
    print p.rstrip(', ')
                    

if __name__ == "__main__":
    printTable()
    similarity(1)
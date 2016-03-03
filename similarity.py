# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:37:24 2016

@author: slide22
"""

import random
from operator import itemgetter

nusers = 1000
nitems = 10
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
    
def itemIntersection(item1, item2):
    customers = []
    
    for i in range(nusers):
        if table[i][item1] == 1 and table[i][item2] == 1:
            customers.append(i)
            
    return customers
    
def itemUnion(item1, item2):
    customers = []
    
    for i in range(nusers):
        if table[i][item1] == 1 or table[i][item2] == 1:
            customers.append(i)
            
    return customers

def similarity():

    similarity = dict()
    # uncomment when is fixed and substitute 0 in whoPurcha... by item    
    # iterate all products
    for item in range(nitems):
        #print '\nItem ' + str(item)
        customers = whoPurchasedItem(item) # foreach item we get who purchased it
        items = dict() # auxiliar variable
        
        for c in customers: # now, we want to know the other items the customers had bought
                            # and store them into items
            for i in range(nitems):
                
                if table[c][i] == 1 and i != item:
                    items[i] = 1
        
        #just print some info
        '''p = "\tOther items bought by customers: "
        for key in items:
            p += str(key) + ", "
        print p.rstrip(', ')'''
        
            
        #calculate similarity
        similarity[item] = list()
        for i2 in items:
            union = len(itemUnion(item, i2))
            intersection = len(itemIntersection(item, i2))
            similarity[item].append((i2, intersection / float(union)))
            
        '''print "\tSimilarities: "
        for tupla in similarity[item]:
            print '\t'+str(tupla[0]) + ': ' + str(tupla[1])'''
            
    return similarity
    
def itemsPurchasedByCustomer(c):
    items = []
    for i in range(nitems):
        if(table[c][i] == 1):
            items.append(i)
    return items
    
def customerRecomendation(c, similarity):
    recomendation = dict()
    items = itemsPurchasedByCustomer(c)
    for item in items:
        
        simItem = sorted(similarity[item], key=itemgetter(1))[0]
        i = 0
        while table[c][simItem[0]] != 1 and i < len(similarity[item]):
            simItem = sorted(similarity[item], key=itemgetter(1))[0]
            i+=1
        if table[c][simItem[0]] != 1:
            recomendation[simItem[0]] = simItem[1];
    return recomendation
    
def customersRecomendation(similarity):
    recomendations = dict()
    
    for c in range(nusers):
        recomendations[c] = customerRecomendation(c, similarity)
    
        '''print 'Customer: ' + str(c)
        for recomendation in recomendations[c]:
            print str(recomendation) + ': '+ str(recomendations[c][recomendation])'''
            
    return recomendations

if __name__ == "__main__":
    printTable()
    similarityDict = similarity()
    #recomendations = customersRecomendation(similarityDict)
    user = 0
    while(user != -1):
        user = input('Introduzca un usuario para ver su recomendacion: ')
        recomendation = customerRecomendation(user, similarityDict)
        
        for recom in recomendation:
                print str(recom) + ': '+ str(recomendation[recom])
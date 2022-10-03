# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 01:17:34 2021

@author: Manish Kumar Goswami
"""

dicto = {
    "apple" : "the round fruit of a tree of the rose family, which typically has thin green or red skin and crisp flesh",
    "lion" :"a large tawny-coloured cat that lives in prides",
    "quarantine" : "a state, period, or place of isolation in which people or animals that have arrived from elsewhere or been exposed to infectious or contagious disease are placed",
    "racist" : " typically one that is a minority or marginalized",
         }

word = input("Enter a number")
count = 0

search = str.lower(word)

for key in dicto:
        if search in key:
            count= count +1
            print(search, ":", dicto[key])
if count == 0:
    print("Search not found Google it")

    
    

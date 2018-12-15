# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 09:26:03 2018

@author: tancr
"""
#%%
#2 points. Imagine you’re creating an application for handling the stock
#of a small shop, and controlling when things go bad in the warehouse.
#Given the following class:
class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality
    
'We have a function that calculates the degrading quality of different'
'products in a shop.'
'Create all the tests you find meaningful for the following function.'
#%%
def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3
#    return product.quality
#'the information is not stored after the function has runned, hence I included a return in it to be able to test it'


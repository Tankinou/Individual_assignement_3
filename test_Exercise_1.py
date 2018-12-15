# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:10:20 2018

@author: tancr
"""

#%%

from Exercise_1 import Product
from Exercise_1 import recalculate_quality

potato = Product("potato", 7)
cheese = Product("cheese", 2)
bacon = Product("bacon", 18)
love = Product("love", 1)

lst = [potato, cheese, bacon, love]
new_quality_lst = [6.5, 0, 18, -2]
quality = []
def test_recalculate_quality ():
    for item in lst:
        recalculate_quality(item)
        quality.append(item.quality)
    
    assert new_quality_lst == quality
















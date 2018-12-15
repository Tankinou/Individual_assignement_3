# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:52:01 2018

@author: tancr
"""
#%%
#2. 5 points. Create an HTTP server and HTTP client to manage a
#phonebook. There should exist the following operations in the phonebook:
#• add a contact (phone + name)
#• get a phone by name
#• delete a phone by name
#• update a phone by name
#Make sure you use JSON to communicate between client and server.

import requests


localhost = "http://127.0.0.1"
#Careate toot     
def add_contact(name,phone_number):
    response = requests.post(localhost+"/addcontact/"+ name +'/'+ phone_number)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code  


def remove_contact(name,phone_number):
    response = requests.post(localhost+"/removecontact/"+ name)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code  

def update_contact(name,phone):
    response = requests.post(localhost+"/updatecontact/"+ name +'/'+ phone)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code  


def show_contact(name,phone):
    response = requests.get(localhost+"/showphone/"+ name +'/'+ phone)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code  




































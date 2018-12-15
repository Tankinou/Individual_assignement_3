# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:40:00 2018

@author: tancr
"""
#%%
#1. 3 points. Using Github’s API, create a function that:
#• takes all repositories from your account
#• prints a short description of each repository, with its name, number
#of stars, main language, and url
import requests

def github_get ():
    
    response = requests.get("https://api.github.com/users/Tankinou/repos").json()
    
    for repos in response:
        if repos["description"] != None:
            print(repos["name"] + " is: " + repos["description"] + " that contains: " + str(repos["stargazers_count"]) + " stars  |  the language is: ' " + str(repos["language"]) +" '  |  the URL is: " +repos["html_url"])
        else:
            print(repos["name"] + " contains: " + str(repos["stargazers_count"]) + " stars  |  the language is: ' " + str(repos["language"]) +" '  |  the URL is: " +repos["html_url"])











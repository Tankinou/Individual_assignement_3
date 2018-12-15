# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 12:52:02 2018

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

from flask import Flask, jsonify

phonebook = {
        "Tan":"12345",
        "Zineb":"54321",
        "GoWithTheFlo":"109876",
        "Dani":"67890"
        }

server = Flask("MyPhonebook")

@server.route("/home")
def home_page():
    return "Welcome to the best assignement"

@server.route("/phonebook")
def get_phonebook():
    return jsonify(phonebook)

@server.route("/addcontact/<name>/<phone_number>")
def add_contact(name,phone_number):
    new_contact = {name:phone_number}
    phonebook.update(new_contact)
    return jsonify(phonebook)

@server.route("/removecontact/<name>")
def remove_contact(name):
    phonebook.pop(name)
    return jsonify("Contact you don't like has been deleted!! Get rid of the negativity in your life! :D")


@server.route("/updatecontact/<name>/<phone>")
def update_contact(name,phone):

    phonebook[name] = phone
    return jsonify("Contact Updated...")



@server.route("/showphone/<name>")
def show_contact(name):
    contact = phonebook[name]
    return jsonify(contact)

server.run()


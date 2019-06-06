# -*- coding: utf-8 -*-
#The requests library is the de facto standard for making HTTP requests in Python. Importing requests package
import requests
#sys module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. Importing sys module
import sys

#Assign the argument passed at runtime to a variable
parameter=sys.argv[1]

#Assign www.omdbapi.com URL to a variable
url='http://www.omdbapi.com/?i=tt3896198&apikey=f7343425'

#The GET method indicates that you’re trying to get or retrieve data from a specified resource. 
response=requests.get(url,parameter)

#Parse the JSON data into a dictionary json_response
json_response = response.json()

#Print the kay-value pair from json_response
for key,value in json_response.items():
    if key == 'Ratings':
        print value[1].get('Source') + ':' +  value[1].get('Value')
# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Kathleen Pham
# kathlep3@uci.edu
# 79281883
#from Profile import *


from pathlib import Path
import os
from Profile import Profile, Post
from ui import printDirectories, outputFiles, searchFile, outputFileExtension, deleteFile, readFile, commandC, commandO, commandE, commandP, allprofile, allposts
from ds_client import send


#if @ weather when a user writes post it should replace 
#transclude function will replace the @ weather with "sunny outside" etc
#1. object = OpenWeather(zipcode, code)
#2. object.setapikey("your api key")
#3. print(object.transclude("hello @ weather") this should print hello sunny


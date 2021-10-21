#Recipe scraper!
#BA's Best Pina Colada

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import numpy as np
from sys import platform

print("*****Starting TLDR*****")

#Control recipe (make sure we don't go too far off the rails): https://www.bonappetit.com/recipe/sweet-and-salty-mango-lassi

#initialize webdrive stuff
win_path = r"C:\Users\Bryn\geckodriver\geckodriver.exe"

options = Options()
options.add_argument('--headless')

# checking if Bryn or Taylor is running this
if platform == 'win32':
	driver = webdriver.Firefox(executable_path=win_path, options=options) # when Bryn's running it (Windows)
else:
	driver = webdriver.Firefox(options=options) # when Taylor's running it (Linux)

#driver.get("https://www.bonappetit.com/recipe/bas-best-pina-colada")

#ask for url
url = str(input("Please enter the URL of the recipe you want to TLDR: "))
driver.get(url)
print('\nOpening recipe...')

#create a dictionary called "recipe"
recipe = {}
table_units = pd.read_csv("units.txt", skiprows=1) #create table for unit scaling

#search for what we need
articler = driver.find_element_by_class_name("recipe")

#get the recipe title
title = articler.find_element_by_xpath('//*[@data-testid="ContentHeaderHed"]').text
recipe["title"] = title # assign to recipe dictionary

bkgd = articler.find_element_by_class_name("content-background")

ingredients_title = bkgd.find_element_by_xpath('//*[@data-testid="IngredientList"]')
print('Getting ingredients...')

#get serving size
servings_text = ingredients_title.find_element_by_tag_name("p").text

servings = [int(s) for s in servings_text.split() if s.isdigit()]
recipe["servings"] = servings[0] #assign to recipe dictionary


# -- TO BE ADDED
# we're thinking about adding a try...except for the ingredients 
# list to account for the recipes where there are subsections.
# as test we can print things to see if it's finding the right stuff

# INGREDIENTS
portions_html = ingredients_title.find_elements_by_tag_name("p")
items_html = ingredients_title.find_elements_by_tag_name("div")

portions, items, measures = [], [], []

# define "is there special equipment" in var special. Start with False
special = False

for x in np.arange(1,len(portions_html)):    #skipping index 0 bc serving size
	if items_html[x].text.upper() == "SPECIAL EQUIPMENT":
	    special = True
	    break
	else:
		portions.append(portions_html[x].text)
		temp_ofThing = items_html[x].text
		pre_words = temp_ofThing.split(" ")
		words = pre_words[0].split(".")
		check = table_units.isin([words[0]]).any().units
		if check:
			measures.append(words[0])
			temp_ofThing = temp_ofThing[len(words[0])+1:] #at some point, ajust output formatting to account for periods
		else:
			measures.append("")
		items.append(temp_ofThing)

#separate out the units
#match them to List
#take them out of "items_html"
#leave in ones that don't match the list


ingredientsList = pd.DataFrame({"amount": portions, "units": measures, "ofThing": items})
recipe["ingredients"] = ingredientsList

# using x result from for loop on line 64
if special == True:
	print('Adding special equipment...')
	special_equip = []
	for y in np.arange((x+1),len(items_html)):
	    special_equip.append(items_html[y].text)
	special_equip = pd.DataFrame({"Addt. Tools": special_equip})
	recipe["special equipment"] = special_equip


# -- TO BE ADDED
# we're thinking about adding a try...except for the instructions
# list to account for the recipes where there are subsections

# INSTRUCTIONS
prep_title = bkgd.find_element_by_xpath('//*[@data-testid="InstructionsWrapper"]/div')
print('Adding instructions...')

stepstxt_html = prep_title.find_elements_by_tag_name("p")
stepstitle_html = prep_title.find_elements_by_tag_name("h3")

steps, steptitles = [], []

# if stepstxt_html and stepstitle_html are not the same length,
# we're assuming there will be more step descriptions than step titles
# so we've added an "if" statement to append an empty string if this happens

for x in np.arange(0,len(stepstxt_html)):
	if x == len(stepstitle_html):
	    steptitles.append("")
	else:
	    steptitles.append(stepstitle_html[x].text+':')
	steps.append(stepstxt_html[x].text)

directions = pd.DataFrame({"steps": steptitles, "details": steps})
recipe["directions"] = directions # add to recipe dictionary


print('Printing recipe in terminal:',end='\n\n')

print('------------------------------------------------------------',end='\n\n')
# running through the keys of the dictionary to print in a pretty way
keys = list(recipe.keys()) # get the list of keys
for key in keys:
	print(key)
	print(recipe[key],end='\n\n') # adds an extra "enter" space between output

print('------------------------------------------------------------')
driver.close() # closing selenium

# ----------------------------------------------- #
# Write results to a text file in a pretty format #
# ----------------------------------------------- #

filename = recipe["title"].replace(" ","-")
filename = filename.replace("'","")

# checking if Bryn or Taylor is running this
if platform == 'win32': slash = '\\'
else: slash = '/'

myfile = open(f'recipes{slash}{filename}.txt','w') # forward slash bc Unix for Taylor

# Writing title & serving size to file
print(recipe['title'], file=myfile)
print(f"Serving size: {recipe['servings']}", file=myfile, end='\n\n')

# Running through tables & writing to file
for key in keys[2:]:
	print(key.upper(), file=myfile)
	table = recipe[key].copy() # getting the table out
	columns = table.columns.values # column names
	if len(columns) > 1:
		for i in table.index.values: # running through row
			print(f'{table.loc[i,columns[0]]} {table.loc[i,columns[1]]}', file=myfile)
	else:
		for i in table.index.values: # running through row
			print(f'{table.loc[i,columns[0]]}', file=myfile)
	print(file=myfile)


# adding URL at the bottom
print(f'\nURL: {url}',file=myfile)

myfile.close()

print(f'\nRecipe download complete!  File saved at recipes{slash}{filename}.txt')

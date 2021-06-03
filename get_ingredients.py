#Recipe scraper!
#BA's Best Pina Colada

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import numpy as np

#initialize webdrive stuff

path = r"C:\Users\Bryn\geckodriver\geckodriver.exe"

options = Options()
options.add_argument('--headless')

#driver = webdriver.Firefox(options=options) # when Taylor's running it (Linux)
driver = webdriver.Firefox(executable_path=path, options=options) # when Bryn's running it (Windows)

#driver.get("https://www.bonappetit.com/recipe/bas-best-pina-colada")

#ask for url
url = str(input("Please enter the URL of the recipe you want to TLDR: "))
driver.get(url)

#create a dictionary called "recipe"
recipe = {}

#search for what we need
articler = driver.find_element_by_class_name("recipe")

#get the recipe title
#title = articler.find_element_by_xpath('//*[@id="main-content"]/article/div[1]/header/div[1]/div[1]/h1').text
title = articler.find_element_by_xpath('//*[@data-testid="ContentHeaderHed"]').text
recipe["title"] = title # assign to recipe dictionary

bkgd = articler.find_element_by_class_name("content-background")

#ingredients_title= bkgd.find_element_by_xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div/div[3]")
ingredients_title = bkgd.find_element_by_xpath('//*[@data-testid="IngredientList"]')

#print(ingredients_title.text)

#get text "Makes 4 servings" to test xpath - success! :)
servings_text = ingredients_title.find_element_by_tag_name("p").text
#servings = servings_text.text.split(" ")[1]

servings = [int(s) for s in servings_text.split() if s.isdigit()]
recipe["servings"] = servings[0] #assign to recipe dictionary

# print("serving size: ",servings[0])
#print(servings_text) # yay this worked!


portions_html = ingredients_title.find_elements_by_tag_name("p")
items_html = ingredients_title.find_elements_by_tag_name("div")

portions, items = [], []

# define "is there special equipment" in var special. Start with False
special = False

for x in np.arange(1,len(portions_html)):    #skipping index 0 bc serving size
    if items_html[x].text.upper() == "SPECIAL EQUIPMENT":
        special = True
        break
    else:
        portions.append(portions_html[x].text)
        items.append(items_html[x].text)

ingredientsList = pd.DataFrame({"amount": portions, "ofThing": items})
recipe["ingredients"] = ingredientsList

# using x result from for loop on line 64
if special == True:
    special_equip = []
    for y in np.arange((x+1),len(items_html)):
        special_equip.append(items_html[y].text)
    special_equip = pd.DataFrame({"Addt. Tools": special_equip})
    recipe["special equipment"] = special_equip

#print(ingredientsList)

prep_title = bkgd.find_element_by_xpath('//*[@data-testid="InstructionsWrapper"]/div')

#print(prep_title.text)

#prep_title = bkgd.find_element_by_xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div/div[4]")


stepstxt_html = prep_title.find_elements_by_tag_name("p")
stepstitle_html = prep_title.find_elements_by_tag_name("h3")

steps, steptitles = [], []

# if stepstxt_html and stepstitle_html are not the same length,
# we're assuming there will be more step descriptions than step step steptitles
# so we've added an "if" statement to append an empty string if this happens

for x in np.arange(0,len(stepstxt_html)):
    if x == len(stepstitle_html):
        steptitles.append("")
    else:
        steptitles.append(stepstitle_html[x].text)
    steps.append(stepstxt_html[x].text)
    #print(stepstitle_html[x].text)
    #print(stepstxt_html[x].text)

directions = pd.DataFrame({"steps": steptitles, "details": steps})
recipe["directions"] = directions # add to recipe dictionary

#print(recipe)

print() # just to add space
# running through the keys of the dictionary to print in a pretty way
keys = list(recipe.keys()) # get the list of keys
for key in keys:
	print(key)
	print(recipe[key],end='\n\n') # adds an extra "enter" space between output

#prototype test - click on Pinterest link in page
##uglyName = bkgd.find_element_by_class_name("social-icons__list-item social-icons__list-item--pinterest social-icons__list-item--circular")
##link = uglyName.find_element_by_tag_name("a")
##link = bkgd.find_element_by_xpath('//a [aria-label = "Share on Pinterest"]')
#allLinks = bkgd.find_elements_by_xpath("//*[contains(@class,'link--pinterest')]")
#link = allLinks[2]
#url = link.get_attribute("href")
#driver.get(url)

#time.sleep(3) #no longer need this, this was for when we opened the browser to test

driver.close()

#Write results to a text file in a pretty format

filename = recipe["title"].replace(" ","-")

myfile = open(f'recipes\{filename}.txt','w') #backslash bc Windows for Bryn

print('Hello', file=myfile)

myfile.close()

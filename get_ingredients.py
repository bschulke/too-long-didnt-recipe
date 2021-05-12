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

driver = webdriver.Firefox(executable_path = path, options=options)

#driver.get("https://www.bonappetit.com/recipe/bas-best-pina-colada")
#ask for url

url = str(input("Please enter the URL of the recipe you want to TLDR: "))

driver.get(url)

#create a dictionary called "recipe"
recipe = {}

#search for what we need
articler = driver.find_element_by_class_name("recipe")

#get the recipe title
title = articler.find_element_by_xpath('//*[@id="main-content"]/article/div[1]/header/div[1]/div[1]/h1').text

recipe["title"] = title # assign to recipe dictionary

bkgd = articler.find_element_by_class_name("content-background")

#ingredients_title= bkgd.find_element_by_xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div/div[3]")
ingredients_title = bkgd.find_element_by_xpath('//*[@data-testid="IngredientList"]/div')

#print(ingredients_title.text)

#get text "Makes 4 servings" to test xpath - success! :)
servings_text = ingredients_title.find_element_by_tag_name("p").text
#servings = servings_text.text.split(" ")[1]
servings = [int(s) for s in servings_text.split() if s.isdigit()]

print("serving size: ",servings[0])
print(servings_text)

recipe["servings"] = servings[0] #assign to recipe dictionary
#print(servings_text) # yay this worked!
#print(servings)

portions_html = ingredients_title.find_elements_by_tag_name("p")
items_html = ingredients_title.find_elements_by_tag_name("div")

portions, items = [], []

for x in np.arange(0,len(portions_html)):    #we WERE skipping index 0 bc serving size, but think we fixed it
    portions.append(portions_html[x].text)
    items.append(items_html[x].text)

ingredientsList = pd.DataFrame({"amount": portions, "ofThing": items})

recipe["ingredients"] = ingredientsList

#print(ingredientsList)

prep_title = bkgd.find_element_by_xpath('//*[@data-testid="InstructionsWrapper"]/div')

#print(prep_title.text)

prep_title = bkgd.find_element_by_xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div/div[4]")


stepstxt_html = prep_title.find_elements_by_tag_name("p")
stepstitle_html = prep_title.find_elements_by_tag_name("h3")

steps, steptitles = [], []

for x in np.arange(0,len(stepstxt_html)):
    print(x)
    steptitles.append(stepstitle_html[x].text)
    steps.append(stepstxt_html[x].text)
    #print(stepstitle_html[x].text)
    #print(stepstxt_html[x].text)

directions = pd.DataFrame({"steps": steptitles, "details": steps})

recipe["directions"] = directions # add to recipe dictionary

print(recipe)

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

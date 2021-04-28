#Recipe scraper!
#BA's Best Pina Colada

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import numpy as np

path = r"C:\Users\Bryn\geckodriver\geckodriver.exe"

options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(executable_path = path, options=options)

driver.get("https://www.bonappetit.com/recipe/bas-best-pina-colada")

articler = driver.find_element_by_class_name("recipe")

bkgd = articler.find_element_by_class_name("content-background")

ingredients_title= bkgd.find_element_by_xpath("/html/body/div[1]/div/main/article/div[2]/div[1]/div/div[3]")

#get text "Makes 4 servings" to test xpath - success! :)
servings_text = ingredients_title.find_element_by_tag_name("p")
servings = servings_text.text.split(" ")[1]
#print(servings_text) # yay this worked!
#print(servings)

portions_html = ingredients_title.find_elements_by_tag_name("p")
items_html = ingredients_title.find_elements_by_tag_name("div")

portions, items = [], []

for x in np.arange(1,len(portions_html)):    #skipping index 0 because that's the serving size
    portions.append(portions_html[x].text)
    items.append(items_html[x].text)

ingredientsList = pd.DataFrame({"amount": portions, "ofThing": items})

print(ingredientsList)

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

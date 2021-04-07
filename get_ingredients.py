#Recipe scraper!
#BA's Best Pina Colada

from selenium import webdriver
import time

path = r"C:\Users\Bryn\geckodriver\geckodriver.exe"

driver = webdriver.Firefox(executable_path = path)

driver.get("https://www.bonappetit.com/recipe/bas-best-pina-colada")

articler = driver.find_element_by_class_name("recipe")

bkgd = articler.find_element_by_class_name("content-background")

#uglyName = bkgd.find_element_by_class_name("social-icons__list-item social-icons__list-item--pinterest social-icons__list-item--circular")
#link = uglyName.find_element_by_tag_name("a")
#link = bkgd.find_element_by_xpath('//a [aria-label = "Share on Pinterest"]')

allLinks = bkgd.find_elements_by_xpath("//*[contains(@class,'link--pinterest')]")

link = allLinks[2]

url = link.get_attribute("href")

driver.get(url)

time.sleep(3)

driver.close()


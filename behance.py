from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, re
from openpyxl import Workbook
from openpyxl import load_workbook
# from pyvirtualdisplay import Display
from selenium import webdriver

#this is not to display the web browser and make it work silently
# display = Display(visible=0, size=(800, 600))
# display.start()

print "Welcome to Behance Scraper"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get('https://www.behance.net/search?field=132&content=users&sort=appreciations&time=week')
elm = driver.find_elements_by_tag_name('html')
elm.send_keys(Keys.END)

usernames = driver.find_elements_by_class_name('user-name')
userlocation = driver.find_elements_by_class_name('user-location')
userfields = driver.find_elements_by_class_name('user-fields')

for name,location,fields in zip(usernames,userlocation,userfields):
	print name.text, location.text, fields.text


driver.quit()
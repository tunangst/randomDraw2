# #import requests library
# import requests
# from bs4 import BeautifulSoup
# #the website URL
# url_link = "https://color.adobe.com/explore"
# result = requests.get(url_link)
# print(result)
# result_json = result.json()
# print(result_json)

# doc = BeautifulSoup(result, "html.parser")

# heading = doc.find(class_ = "Theme__theme___2NcED")

# from selenium import webdriver
# import time
# import string
# import pandas as pd

# driver = webdriver.Chrome('/Users/tru/Desktop/chromedriver_mac64/chromedriver')
# searchAddress = 'https://color.adobe.com/explore'

# elements = driver.find_element(By.CLASS_NAME, "Theme__theme___2NcED")  
# driver.get(searchAddress)
# print(elements)

# time.sleep(80)

import sys
print(sys.path)
from selenium import webdriver
import time
import pandas as pd

color_theme_array = []

driver = webdriver.Chrome('C:\Users\snype\Documents\chromedriver_win32(1)\chromedriver.exe')

searchAddress = 'https://color.adobe.com/explore'
driver.get(searchAddress)

# FILTER THROUGH ONLY SWATCHES OF COLOR THEME
# <BUTTON id="react-spectrum-12-trigger" ... >.CLICK
# DROP DOWN
# <LI id="react-spectrum-2685" ...>.CLICK OR HOVER IF OPTION
# SIDE MENU
# <DIV CLASS=spectrum-Popover switches instanced id
# <ul id='react-spectrum-525'
# <li>[0]
#

time.sleep(2)

# find and remove splash screen overlay
splash_screen_close_btn = driver.find_element_by_xpath(
    "//*[contains(@class, 'closeButton')]").click()

# we want all of the themes and no gradients etc.
# find all sources button and press it
all_sources_btn = driver.find_element_by_xpath(
    "//*[contains(text(), 'All Sources')]")
all_sources_btn.click()
time.sleep(1)
# find color themes tab and click on it
color_themes_btn = driver.find_element_by_xpath(
    "//*[contains(text(), 'Color Themes')]")
color_themes_btn.click()
time.sleep(1)
# find all time tab and click on it
all_time_btn = driver.find_element_by_xpath(
    "//*[contains(text(), 'All Time')]")
all_time_btn.click()

time.sleep(2)


current_page_number = 0
loop_increment = 10000
active_loop = True
while (active_loop or loop_increment <= 0):
    time.sleep(2)
    # find all color cards on page
    color_theme_cards = driver.find_elements_by_xpath(
        "//*[contains(@class, 'Theme__theme')]")
    # print(color_theme_cards)
    # print(len(color_theme_cards))

    # loop over cards
    for card in color_theme_cards:
        color_swatch = []
        # find all color divs
        colors = card.find_elements_by_css_selector("div")
        # print(len(colors))
        # loop over all color in the swatch and create an array swatch
        for color in colors:
            style = color.get_attribute("style")
            style_length = len(style)
            rgb = style.find(' ') + 1
            rgb_string = style[rgb: style_length - 1]

            # convert to ascii to remove u'rgb(1,1,1)'
            ascii_rgb_string = rgb_string.encode('ascii')

            color_swatch.append(ascii_rgb_string)

        color_theme_array.append(color_swatch)
        print(len(color_theme_array))

    # find next button
    time.sleep(1)
    next_btn = driver.find_element_by_xpath(
        "//span[text() = 'Next']")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    next_btn.click()

    # get page number from url
    page_number = driver.current_url[-1]
    if current_page_number >= page_number or current_page_number == 125:
        active_loop = False
    print(page_number)

    color_theme_cards = ''
    current_page_number += 1
    loop_increment -= 1

with open("themes.txt", mode="wt") as f:
    f.write(str(color_theme_array))

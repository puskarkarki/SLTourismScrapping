import os
import selenium
from selenium import webdriver

website = 'https://www.welcomenepal.com/things-to-do/trekking.html'
path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
page_titles = driver.find_elements_by_tag_name('h2')
title_description = driver.find_elements_by_tag_name('h4')
for description in title_description:
    print(description.text)

page_headers = driver.find_elements_by_tag_name('div')
header = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/h1').text
print(header)
page_content = driver.find_elements_by_tag_name('p')
for information in page_content:
    print(information.text)

title_description = driver.find_elements_by_tag_name('h4')
for description in title_description:
    print(description.text)

links = driver.find_elements_by_xpath('.//a')

for a in links:
    print(a.get_attribute('href'))






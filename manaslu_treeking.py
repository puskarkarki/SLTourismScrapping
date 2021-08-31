import os
import selenium
from selenium import webdriver

website = 'https://www.welcomenepal.com/things-to-do/trekking.html'
path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
page_titles = driver.find_elements_by_tag_name('h2')
"""""for title in page_titles:
    print(title.text)"""

page_headers = driver.find_elements_by_tag_name('div')
header = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/h1').text
print(header)
page_content = []
for information in page_headers:
    page_content1 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[2]').text
    page_content2 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[3]').text
    page_content3 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[4]').text
    page_content4 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[5]').text
    page_content5 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[7]').text
    page_content6 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[9]').text
    page_content7 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[10]').text
    page_content8 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[12]').text
    page_content9 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[13]').text
    page_content10 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[15]').text
    page_content11 = information.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/p[16]').text
    page_content.append(page_content1)
    page_content.append(page_content2)
    page_content.append(page_content3)
    page_content.append(page_content4)
    page_content.append(page_content5)
    page_content.append(page_content6)
    page_content.append(page_content7)
    page_content.append(page_content8)
    page_content.append(page_content9)
    page_content.append(page_content10)
    page_content.append(page_content11)
    print(page_content1)
"""print(page_content2)
    print(page_content3)
    print(page_content4)
    print(page_content5)
    print(page_content6)
    print(page_content7)
    print(page_content8)
    print(page_content9)
    print(page_content10)
    print(page_content11)"""




"""title_description = driver.find_elements_by_tag_name('h4')
for description in title_description:
    print(description.text)"""

"""""Extracting the image links in current pages"""

"""images = driver.find_elements_by_tag_name('img')

for image in images:
    print(image.links)
""""""driver.quit()"""



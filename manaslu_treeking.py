from selenium import webdriver

website = 'https://www.welcomenepal.com/places-to-see/manaslu.html'
path = '/usr/bin/chromedriver'
driver = webdriver.Chrome(path)
driver.get(website)
page_title = driver.find_element_by_xpath('//*[@id="carousel-example-generic"]/div/div/div/h2')
page_title.text
print(page_title.text)
sub_title = driver.find_element_by_xpath('//*[@id="carousel-example-generic"]/div/div/div/h4')
print(sub_title.text)
driver.quit()



from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

#we can select our browser (we are going to select Chrome)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.amazon.com.mx')
#this two lines need to be together
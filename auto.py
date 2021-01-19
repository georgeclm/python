from re import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.youtube.com/')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Unbox Therapy')
searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()

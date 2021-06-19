#youtube
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(PATH)

name = input("Enter name of video: ")

driver.get('https://www.youtube.com/')

time.sleep(2)

search = driver.find_element_by_id("search")
search.click()

search.send_keys(name)
search.send_keys(Keys.ENTER)

time.sleep(2)

firstresult = driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
firstresult.click()



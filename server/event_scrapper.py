from selenium import webdriver
from selenium.webdriver.common.by import By

events_dict = {"Football": "https://gohuskies.com/sports/football/schedule/2024"}


driver = webdriver.Chrome()
print("hello")

driver.get(events_dict["Football"])

title = driver.title
driver.implicitly_wait(0.5)


message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()

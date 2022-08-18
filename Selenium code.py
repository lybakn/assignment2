from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r'C:\Users\User\PycharmProjects\chromedriver.exe')
driver.get("https://www.facebook.com/login/")
print(driver.title)
driver.close()






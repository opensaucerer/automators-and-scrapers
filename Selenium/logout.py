from selenium import webdriver
from time import sleep

# instantiating the chrome driver
path = r"C:\src\chromedriver.exe"
driver = webdriver.Chrome(path)

# reading the password file
data = open('./passwords.csv').readlines()

# visiting the login page
url = 'http://gateway.futa.edu.ng/logout'
driver.get(url)

# performing a graceful exit
driver.quit()
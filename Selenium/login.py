from selenium import webdriver
from time import sleep

# instantiating the chrome driver
path = r"C:\src\chromedriver.exe"
driver = webdriver.Chrome(path)

# reading the password file
data = open('./passwords.csv').readlines()

# visiting the login page
url = 'http://gateway.futa.edu.ng/login'
driver.get(url)

# exiting gracefully is user is already logged in
if 'status' in driver.current_url:
    driver.quit()

# setting the iterator
i = 0

# entering the password and username into the input box
def login(username, password):

    # getting the elements from the DOM
    passwordInput = driver.find_elements_by_name('password')[1]
    usernameInput = driver.find_elements_by_name('username')[1]
    submit = driver.find_element_by_tag_name('button')

    # attempting to login
    usernameInput.clear()
    usernameInput.send_keys(username + '@futa.edu.ng')
    passwordInput.clear()
    passwordInput.send_keys(password)
    submit.click()
    
    # setting conditional for graceful exit
    if 'login' in driver.current_url:
        return False
    return True



while i < len(data):
    # processing login data from the CSV file
    new_data = data[i].strip().split(', ')
    username = new_data[0]
    password = new_data[1]
    res = login(username, password)
    # incrementing the iterator
    i+=1
    # exiting gracefully upon successful login
    if res:
        driver.quit()
    # shifting to next iteration if login fails at first try
    else:
        sleep(3)
        continue

# graceful exit on successful While Loop execution
driver.quit()

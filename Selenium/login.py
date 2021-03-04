from selenium import webdriver

# instantiating the chrome driver
path = r'C:\Users\Samperfect\Downloads\Codes\Libraries\Drivers\chromedriver.exe'
driver = webdriver.Chrome(path)

# reading the password file
un = open('./names.csv').readlines()
pw = open('./password.csv').readlines()

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


while i < len(un):
    # processing login data from the CSV file
    username = un[i].strip()
    password = pw[i].strip()
    res = login(username, password)
    # incrementing the iterator
    i += 1
    # exiting gracefully upon successful login
    if res:
        driver.quit()
    # shifting to next iteration if login fails at first try
    else:
        continue

# graceful exit on successful While Loop execution
driver.quit()

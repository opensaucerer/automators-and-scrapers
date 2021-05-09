import requests
from datetime import datetime
import csv
from bs4 import BeautifulSoup as bs

start_time = datetime.utcnow()

try:
    url = 'https://www.hospitalsafetygrade.org/all-hospitals'

    response = requests.get(url).content

    soup = bs(response, "html.parser")
    # opening main page
    try:
        links = soup.select('#BlinkDBContent_849210 ul li a')

    except:
        print("ERROR:  Couldn't find any hospital")

    # start a for loop
    print(len(links))
    i = 2698
    # for link in links:
    while i < 2736:

        # opening leap frog page
        try:
            print("Visiting -->  " + links[i]['href'])
            new_response = requests.get(links[i]['href']).content

            soup = bs(new_response, "html.parser")

            redir_one = soup.select('#survey-results-container a')[0]['href']

        except:
            print("ERROR: Couldn't open hospital Leap Frog Page")

        # Opening survery results page
        try:
            print('  Redirecting to --->  ' + redir_one)
            an_response = requests.get(redir_one).content

            soup = bs(an_response, "html.parser")

        except:
            print("ERROR: Couldn't open survey results")

            # getting the name of the hospital
        try:
            name = soup.find_all(
                'h1', class_='quote-large blue margin-bottom-20')[0].text
        except:
            name = ""

        # getting the address of the hospital
        try:
            address = soup.select('.facility-address strong')[0].text.replace(
                '\n', '').replace('                        ', '')
        except:
            address = ""

        try:
            website = soup.select(
                '.margin-bottom-40')[0].select('tr')[1].select('td a')[0]['href']
        except:
            website = ""

        with open('hospital.csv', 'a') as h:
            writer = csv.writer(h, delimiter='|')
            writer.writerow([name, address, website])
        # print(name, address, website)

        print(f'SUCCESS --> HOSPITAL INFO GOTTEN ---> {i}')

        print(f'TIME ELAPSED:  { datetime.utcnow() - start_time}')

        i += 1


except ConnectionError:
    print('Network Error --> Try Again')
except ConnectionAbortedError:
    print('Network Error --> Try Again')
except ConnectionRefusedError:
    print('Network Error --> Try Again')
except ConnectionResetError:
    print('Network Error --> Try Again')

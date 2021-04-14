from bs4 import BeautifulSoup
import requests
import time


page = 53
while(page <= 53):

    send_request = requests.get(
        "https://www.realtor.com/realestateagents/new-york_ny/pg-" + str(page))

    print("https://www.pigiame.co.ke/cars?p=" + str(page))

    response = send_request.content

    soup = BeautifulSoup(response, "html.parser")
    # print(soup.prettify())

    names = soup.find_all('div', class_='agent-phone hidden-xs hidden-xxs')

    l = []
    for name in names:
        print(name)

    # name = soup.find_all('div', class_='agent-name text-bold')
    # num = soup.find_all('div', class_='agent-phone hidden-xs hidden-xxs')

    # names = []

    # nums = []

    # for nu in num:
    #     nu = nu.text
    #     nu = nu.strip()
    #     nums.append(nu)

    # for na in name:
    #     na = na.text
    #     na = na.strip()
    #     names.append(na)

    # for x in nums:
    #     f = open('nums.txt', 'a')
    #     f.write(f'{x}')
    #     f.write('\n')
    #     f.close()

    # for y in names:
    #     f = open('names.txt', 'a')
    #     f.write(f'{y}')
    #     f.write('\n')
    #     f.close()

    page += 1

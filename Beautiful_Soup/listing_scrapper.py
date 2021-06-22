from bs4 import BeautifulSoup
import requests

page = 1
while(page <= 1):

    send_request = requests.get(
        "https://www.pigiame.co.ke/cars?p=" + str(page))

    print("https://www.pigiame.co.ke/cars?p=" + str(page))
    link = "https://www.pigiame.co.ke/cars?p=" + str(page)

    response = send_request.content

    soup = BeautifulSoup(response, "html.parser")
    # print(soup.prettify())

    items = soup.find_all('span', class_='listing-card__header__tags__item')
    names = soup.find_all('div', class_='listing-card__header__title')
    nums = soup.find_all('a', class_='listing-card__contact__number-inner')

    year = []
    y = []
    for item in items:
        item = item.text
        tem = item.strip("\n")
        year.append(tem)

    i = 0
    while(i < len(year)):

        for x in year[i]:

            if str(2) in str(x):
                y.append(year[i])
            break
        i += 1

    for name in names:
        name = name.text
        name = name.strip('\n')

        for num in nums:
            num = num.text
            num = num.strip('\n')

            for x in y:
                x = str(x)

        f = open('name.txt', 'a')
        f.write(f'{name}, {x}, {num}, {link}')
        f.write('\n')
        f.close()

    page += 1

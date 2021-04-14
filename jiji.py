from bs4 import BeautifulSoup as bs
import requests


page = 1

while page <= 10:

    url = "https://deals.jumia.co.ke/cars?page=" + str(page)
    print(url)
    request = requests.get(url, allow_redirects=True)

    response = request.content

    soup = bs(response, "html.parser")

    posts = soup.find_all('a', class_="post-link post-vip")

    def get_number():
        global number
        number = str(numbers)
        number = number.split('<a href="tel:')
        number = str(number[1])
        number = number.split('">')
        number = number[0]
        return number

    def get_year():

        year_data = ""
        global year
        for year in years:

            year = str(year.text)
            year = year.split("Year")
            year_data = str(year[1])

            year = str(year_data[0] + year_data[1] +
                       year_data[2] + year_data[3])
            return year

    for post in posts:
        name = post.text
        link = "https://deals.jumia.co.ke" + post['href']

        request = requests.get(link, allow_redirects=True)
        response = request.content
        soup = bs(response, "html.parser")

        global years
        years = soup.find_all("div", class_="new-attr-style")
        global numbers
        numbers = soup.find("div", class_="phone-box show")
        get_number()
        get_year()

        f = open('data.txt', 'a')
        f.write(f'{name}, {year}, {number}, {link}')
        f.write('\n')
        f.close()

    page += 1

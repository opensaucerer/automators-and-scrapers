# import requests as r
# from bs4 import BeautifulSoup as bs


# url = "https://www.yfgnigeria.org/members"

# request = r.get(url)
# response = request.content

# print(response)

f = open("names.txt", "r")
i = 0
while i < 4:
    line = f.readline()
    new_line = line.split(',')
    print(new_line)
    i += 1

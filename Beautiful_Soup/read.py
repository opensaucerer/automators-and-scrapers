f = open('data.txt', 'r')


i = 0

while i < 11:
    data = f.readline()
    data = str(data)
    if "toyota" in data.lower():
        print(data)
    i += 1

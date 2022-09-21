import requests


def value(name2, money):
    print('Checking the cache...')

    if name2 in currencies:
        print('Oh! It is in the cache!')
        rate = currencies[name2]
    else:
        print("Sorry, but it is not in the cache!")
        x = r[name2]
        rate = x["rate"]
        currencies[name2] = rate

    print('You received', round(money * rate, 2), name2.upper() + '.')


currencies = {}

name1 = input().lower()
r = requests.get(f'http://www.floatrates.com/daily/{name1}.json').json()

if name1 != 'eur':
    e = r["eur"]
    add = e["rate"]
    currencies["eur"] = add

if name1 != 'usd':
    u = r["usd"]
    add = u["rate"]
    currencies["usd"] = add

for i in range(5):

    Y = input().lower()
    if Y == "":
        break
    Z = float(input())
    value(Y, Z)

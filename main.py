from flask import Flask, render_template
from urllib.request import urlopen
from json import loads


app = Flask(__name__)
@app.route('/')


def index():
    global list_of_currencys
    list_of_currencys = []
    get_privat_valute()
    return render_template('index.html', list_of_currencys=list_of_currencys)


def get_privat_valute():
    r = loads(urlopen("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").read())
    
    for d in r:    
        for key in d:
            if key == "ccy":
                name = d[key]
                print(key, " ",d[key])
            elif key == "buy":
                buy = round(float(d[key]),2)
                print(key, " ",d[key])
            elif key == "sale":
                sale = round(float(d[key]),2)
                print(key, " ",d[key])

        list_of_currencys.append(Currency(name, buy, sale))


class Currency():
    def __init__(self, name_of_currency, buy_price, sale_price):
        self.name = name_of_currency
        self.buy = buy_price
        self.sale = sale_price


if __name__ == "__main__":
    app.run(debug=True)

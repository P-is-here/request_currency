from requests_html import HTMLSession
from flask import Flask, render_template

session = HTMLSession()
app = Flask(__name__)
@app.route('/')


def index():
    global list_of_currencys
    list_of_currencys = []
    get_privat_valute()
    return render_template('index.html', list_of_currencys=list_of_currencys)


def get_privat_valute():
    r = session.get('https://privatbank.ua/rates-archive')
    r = r.html.find('.currency-pairs')[0:3]
    
    for i, value in enumerate(r):
       r[i] = value.text
    
    for el in r:
        name = el[0:3]
        buy = ""
        sell = ""
        mode = 0

        for symbol in el:
            if symbol.isdigit() or symbol==".":
                if mode in (0, 1):
                    mode = 1
                    buy += symbol
                else:
                    sell += symbol
            elif mode == 1:
                    
                    mode = 2
        
        list_of_currencys.append(Currency(name, buy, sell))


class Currency():
    def __init__(self, name_of_currency, buy_price, sell_price):
        self.name = name_of_currency
        self.buy = buy_price
        self.sell = sell_price


if __name__ == "__main__":
    app.run(debug=True)

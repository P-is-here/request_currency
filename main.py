#from requests_html import HTMLSession
from flask import Flask, render_template
from urllib.request import urlopen
import json


#session = HTMLSession()
app = Flask(__name__)
@app.route('/')


def index():
    global list_of_currencys
    list_of_currencys = []
    get_privat_valute()
    return render_template('index.html', list_of_currencys=list_of_currencys)


def get_privat_valute():
    #r = session.get('https://api.privatbank.ua/')
    r = json.loads(urlopen("https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5").read())
    print(r)
    #r = r.html.find("body")
    #for i, value in enumerate(r):
    #   r[i] = value.text
    
    for el in range(3):
        name = ""
        buy = ""
        sale = ""
        list_of_currencys.append(Currency(name, buy, sale))
        '''
        for tag in el:
            if tag == 'ccy':
                name = el.get('ccy')
            elif tag == 'buy':
                buy = el.get('buy')
            elif tag == 'sale':
                sale = el.get('sale')
        '''


class Currency():
    def __init__(self, name_of_currency, buy_price, sale_price):
        self.name = name_of_currency
        self.buy = buy_price
        self.sale = sale_price


if __name__ == "__main__":
    app.run(debug=True)

from lib2to3.pytree import convert
import requests
from tkinter import *

def currency_convert(fromCurrency, toCurrency, currency):
	url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

	querystring = {"from":fromCurrency,"to": toCurrency,"amount":currency}

	headers = {
		"X-RapidAPI-Key": "eac0522f5dmsh2b808ebf038045dp169384jsnba8c48fe4dcb",
		"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())
# currency_convert("USD","EUR", 100)


root = Tk()

root.geometry("300x400")

title = "Currency Converter"
root.title(title)
titleLabel = Label(root, text=title)
titleLabel.pack(pady=10)

amountLabel = Label(root, text="Amount:")
amountLabel.place(width=50, height=10, x=20, y=30)
currencyEntry = Entry(root)
currencyEntry.place(width=200, x= 50, y=50)

currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'HKD', 'NZD']

fromFrame = Frame(root)
toFrame = Frame(root)
fromClicked = StringVar()
fromClicked.set(currencies[3])
toClicked = StringVar()
toClicked.set(currencies[1])
fromLabel = Label(root, text="From currency")
toLabel = Label(root, text="To currency")
fromDropdown = OptionMenu(root, fromClicked, *currencies)
toDropdown = OptionMenu(root, toClicked, *currencies)
fromDropdown.config(width=10)
toDropdown.config(width=10)

fromFrame.place(width=200, height=30, x=50, y=100)
toFrame.place(width=200, height=30, x=50, y=130)
fromLabel.pack(side="left")
fromDropdown.pack(side="right")
toLabel.pack(side="left")
toDropdown.pack(side="right")

convertButton = Button(root, text="Convert", command=lambda f = fromDropdown, t = toDropdown, c = currencyEntry: currency_convert(f.get(), t.get(), c.get())
convertButton.place(width=60, height=30, x=130, y=170)


getResult = Label(root)
getResult.place(width=80, height=30, x=110, y=220)

root.mainloop()
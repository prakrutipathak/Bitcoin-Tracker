import requests
import tkinter as tk
from datetime import datetime

def trackBitcoin():
    url ="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    labelPrice.config(text = str(price) + " $")
    labelTime.config(text="UPDATED AT:" + time)
    canvas.after(1000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("400x300")
canvas.title("BITCOIN TRACKER")

f1 = ("Britannic Bold",25,"bold")
f2 = ("Berlin Sans FB",22,"normal")
f3 = ("Berlin Sans FB",18,"normal")

label = tk.Label(canvas, text="BITCOIN PRICE",fg="brown", font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady=10)

labelTime =tk.Label(canvas, font = f3)
labelTime.pack(pady=10)

trackBitcoin()

canvas.mainloop()
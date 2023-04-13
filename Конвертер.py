from PyQt5 import Qt
from PyQt5.QtWidgets import *
import requests
import pandas as pd

url = "https://fapi.binance.com/fapi/v1/premiumIndex"
param = {'symbol' : 'ETHUSDT'}

r = requests.get(url, params=param)

if r.status_code == 200:
    print(r.json())
    data = r.json()
    print(data)
else:
    print("Помилка")

app = QApplication([])
window = QWidget()
window.setWindowTitle("Конвертер валют")
window.resize(300,600)

btnkonvert = QPushButton("Конвертувати")
btnremove = QPushButton("Стерти")

label = QLabel("КОНВЕРТЕР ВАЛЮТ")
label2 = QLabel("Введи валюту")
label3 = QLabel("Результат")

choose_currency = QLineEdit()
writecurrency= QLineEdit()
outcurrency = QLineEdit()


mainline = QVBoxLayout()
Hline = QHBoxLayout()
mainline.addWidget(label)
mainline.addWidget(label2)

app.setStyleSheet("""
        QWidget{
            #background-image : url("Конвертер Бінанс/Binance_Logo.jpeg")
        }
    """)

Hline.addWidget(writecurrency)
Hline.addWidget(choose_currency)


window.setLayout(mainline)
mainline.addLayout(Hline)

mainline.addWidget(label3)
mainline.addWidget(outcurrency)
mainline.addWidget(btnkonvert)
mainline.addWidget(btnremove)

window.show()
app.exec_()
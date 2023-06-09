from PyQt5 import Qt
from PyQt5.QtWidgets import *
import requests
import pandas as pd



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
outcurrency.setReadOnly(True)

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
#mainline.addWidget(btnremove)

def course():
    val1 = choose_currency.text()
    val2 = writecurrency.text()
    url = "https://fapi.binance.com/fapi/v1/premiumIndex"
    param = {'symbol' : val1 + val2}

    r = requests.get(url, params=param)

    if r.status_code == 200:
        print(r.json())
        data = r.json()
        print(data)
    else:
        outcurrency.setText("Помилка")
    
btnkonvert.clicked.connect(course)
window.show()
app.exec_()
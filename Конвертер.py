from PyQt5 import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.setWindowTitle("Конвертер валют")
window.resize(300,600)

btnkonvert = QPushButton("Конвертувати")
btnremove = QPushButton("Стерти")

label = QLabel("КОНВЕРТЕР ВАЛЮТ")

takevalut = QLineEdit()
outvalut = QLineEdit()


mainline = QVBoxLayout()
Hline = QHBoxLayout
mainline.addWidget(label)
mainline.addWidget(takevalut)

mainline.addWidget(outvalut)
mainline.addWidget(btnkonvert)
mainline.addWidget(btnremove)


window.setLayout(mainline)


window.show()
app.exec_()
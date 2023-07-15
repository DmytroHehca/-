from PyQt5.QtWidgets import *
import main

data = {
    "user":{
        "швидкість": 5
    }
}

app = QApplication([])

window = QWidget()
btn = QPushButton("Play")

mainLine = QVBoxLayout()
mainLine.addWidget(btn)
def level1():

    main.playgame()

btn.clicked.connect(level1)

window.setLayout(mainLine)
window.show()
app.exec_()
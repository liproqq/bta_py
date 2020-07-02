import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rechner')
        self.resize(200, 200)

        self.line1 = QLineEdit()
        self.line2 = QLineEdit()
        self.pb1 = QPushButton('+')
        self.pb1.clicked.connect(self.calculate1)
        self.pb2 = QPushButton('-')
        self.pb1.clicked.connect(self.calculate2)
        self.pb3 = QPushButton('/')
        self.pb1.clicked.connect(self.calculate3)
        self.pb4 = QPushButton('*')
        self.pb1.clicked.connect(self.calculate4)
        self.output = QLabel()

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.pb1)
        vbox1.addWidget(self.pb2)
        vbox1.addWidget(self.pb3)
        vbox1.addWidget(self.pb4)

        hbox = QHBoxLayout()
        hbox.addWidget(self.line1)
        hbox.addLayout(vbox1)
        hbox.addWidget(self.line2)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.output)
        self.setLayout(vbox)
        self.show()

    def calculate1(self):
        number1 = int(self.line1.text())
        number2 = int(self.line2.text())
        antwort = str(number1 + number2)
        self.output.setText(antwort)
        self.output.repaint()

    def calculate2(self):
        number1 = int(self.line1.text())
        number2 = int(self.line2.text())
        antwort = str(number1 - number2)
        self.output.setText(antwort)
        self.output.repaint()

    def calculate3(self):
        number1 = int(self.line1.text())
        number2 = int(self.line2.text())
        antwort = str(number1 / number2)
        self.output.setText(antwort)
        self.output.repaint()

    def calculate4(self):
        number1 = int(self.line1.text())
        number2 = int(self.line2.text())
        antwort = str(number1 * number2)
        self.output.setText(antwort)
        self.output.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    sys.exit(app.exec_())

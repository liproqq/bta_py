import os
import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QComboBox, QLineEdit, QTextEdit, QLabel,  QCheckBox



class Window(QWidget):

    def __init__(self):
        super().__init__()
        sshFile=os.path.join(os.path.dirname(__file__), 'mystylesheet.css')
        with open(sshFile,"r") as fh:
            self.setStyleSheet(fh.read())
        self.setWindowTitle('My Skunk Layout')


        #mywidgets
        self.labelLine = QLabel("Hier steht eine Linie")
        self.labelText = QLabel("Ein langer Text")
        self.line = QLineEdit()
        self.line.setPlaceholderText("Titel für irgendwas")
        self.text = QTextEdit()
        self.text.setPlaceholderText("Hier kann man ganz viel Text reinschreiben")

        self.okButton = QPushButton('Klick mich')

        self.rb1 = QRadioButton('Radio 1')
        self.rb2 = QRadioButton('Radio 2')

        self.combo = QComboBox()
        self.combo.addItem("Combo 1")
        self.combo.addItem("Combo 2")
        self.combo.addItem("Combo 3")
        self.combo.addItem("Combo 4")

        self.cB1 = QCheckBox("Checkbox 1")
        self.cB2 = QCheckBox("Checkbox 2")
        self.cB3 = QCheckBox("Checkbox 3")

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.rb1)
        vbox1.addWidget(self.rb2)
        vbox1.addWidget(self.cB1)
        vbox1.addWidget(self.cB2)
        vbox1.addWidget(self.cB3)
        vbox1.addWidget(self.labelLine)
        vbox1.addWidget(self.okButton)
        vbox1.addWidget(self.combo)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.text)
        vbox2.addWidget(self.line)


        hbox = QHBoxLayout()
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        self.setLayout(hbox)
        #showWindow
        icon = os.path.join(os.path.dirname(__file__), 'skunk.png')
        self.setWindowIcon(QIcon(icon))
        self.show()

if __name__ == '__main__':


    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

import sys
import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QComboBox, QLineEdit, QTextEdit, QLabel,  QCheckBox

class Window(QWidget):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('Layout')
        self.resize(250, 50)
        
        self.verify = QPushButton("OK")
        self.verify.clicked.connect(self.checkOkay)
        self.falsify = QPushButton("Not OK")
        self.falsify.clicked.connect(self.checkNotOkay)
        self.result = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.verify)
        layout.addWidget(self.falsify)
        layout.addWidget(self.result)
        self.setLayout(layout)
        self.show()
    def checkOkay(self):
        self.result.setText("Alles Roger, Steve!")
    def checkNotOkay(self):
        self.result.setText("Captain America to the rescue, immediately!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QWidget, QPushButton
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200,200)
        self.setWindowTitle('Button horizontal')
        #Widgets
        self.cancelButton = QPushButton("Cancel")
        self.okButton = QPushButton("OK")
        #horizontales Layout
        hBox = QHBoxLayout()
        hBox.addWidget(self.okButton)
        hBox.addWidget(self.cancelButton)
        self.setLayout(hBox)
        self.show()
#Hauptprogramm
app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
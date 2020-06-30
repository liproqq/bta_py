import sys

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QCheckBox, QLabel, QPushButton, QComboBox, QTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Widget Demo')
        # self.resize(300, 300)
        self.rb1 = QRadioButton('Radiobutton 1')
        self.rb2 = QRadioButton('Radiobutton 2')
        self.cb1 = QCheckBox('Checkbox 1')
        self.cb2 = QCheckBox('Checkbox 2')
        self.cb3 = QCheckBox('Checkbox 3')
        self.label = QLabel('Das ist ein Label')
        self.pb = QPushButton('Schaltfläche')
        self.combo = QComboBox()
        self.combo.addItem('Option 1')
        self.combo.addItem('Option 2')
        self.combo.addItem('Option 3')
        self.combo.addItem('Option 4')
        self.text = QTextEdit()
        self.text.setPlaceholderText('Das ist ein mehrzeiliges Texteditor-Feld. Es dient der Ein- und Ausgabe von Texten.')
        self.line = QLineEdit()
        self.line.setPlaceholderText('Das ist eine Eingabezeile.')
        grid = QGridLayout()
        grid.addWidget(self.text, 0, 1, 7, 1)   # 3 = zeile, 4 = spalte
        grid.addWidget(self.line, 7, 1)
        grid.addWidget(self.rb1, 0, 0)
        grid.addWidget(self.rb2, 1, 0)
        grid.addWidget(self.cb1, 2, 0)
        grid.addWidget(self.cb2, 3, 0)
        grid.addWidget(self.cb3, 4, 0)
        grid.addWidget(self.label, 5, 0)
        grid.addWidget(self.pb, 6, 0)
        grid.addWidget(self.combo, 7, 0)
        self.setLayout(grid)
        self.show()
        
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
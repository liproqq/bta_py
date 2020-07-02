 # BTA Python Grundkurs Projekttag 3
# Aufgabe 1:
# Zahlentest - Erstelle eine GUI, mit einer Eingabe,
# welche testet ob der eingegebene Wert eine Zahl ist.
# (gemäß Abbildung)

print("-------------------------------------------")
print("TA Python Grundkurs Projekttag 3")
print("Aufgabe 1----------------------------------")
print()


# Module sys und PyQt5 importieren
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtWidgets import QPushButton, QVBoxLayout


# Fenster "Zahlentest" anlegen
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Zahlentest')

# Widgets definieren
        self.antwort = QLineEdit()
        self.frage = QLabel('Ist die Eingabe eine Nummer ?')
        self.ergebnis = QLabel()
        self.senden = QPushButton('Testen')
        self.senden.clicked.connect(self.isnummer)

# Layout anlegen und Widgets einfügen
        layout = QVBoxLayout()
        layout.addWidget(self.antwort)
        layout.addWidget(self.senden)
        layout.addWidget(self.frage)
        layout.addWidget(self.ergebnis)

        self.setLayout(layout)
        self.show()

# # Variante 1 Testfunktion mit ISDIGIT -> keine float Prüfung
#     def isnummer(self):
#         text = self.antwort.text()
#         if text.isdigit():
#             self.ergebnis.setText('Ja')
#         else:
#             self.ergebnis.setText('Nein')



# Variante 2 Testfunktion mit ISDIGIT und FLOAT Prüfung (replacing 1 x "." !!)
    def isnummer(self):
        text = self.antwort.text()
        if text.isdigit():
            self.ergebnis.setText('Ja inty')
        elif text.replace(".","",1).isdigit():
            self.ergebnis.setText('Ja floaty')
        else:
            self.ergebnis.setText('Nein')




# Mainbereich

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    sys.exit(app.exec_())

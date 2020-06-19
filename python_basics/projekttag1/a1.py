# Lies einen Buchstaben ein.
# 1) Wiederhole dies solange, bis der eingegebene Buchstabe ein „j“ oder ein „J“ ist.
# 2) Wiederhole es solange, bis die Eingabe „j“, „J“, „ja“, „Ja“, „jA“ oder „JA“ ist.

eingabe = ""

while eingabe.lower() != "j":
    eingabe = input("Bitte j eingeben: ")

print("Danke")

print("---------------------------------------\nTeil 2:")

eingabe = ""

while eingabe.lower() != "j" and eingabe.lower() != "ja":
    eingabe = input("Bitte bestätigen: ")

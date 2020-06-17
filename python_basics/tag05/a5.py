# Aufgabe 5:
#
# Schreibe ein Programm welches mit 'input()' einen String bekommt.
# Und testen soll ob der string eines der folgenden Zeichen als letztes hat:
#
# '.', '!', '?'
#
# Nutze boolsche Algebra (and oder or verbindungen in einer if-Anfrage.)

satzzeichen = ['.', '!', '?']


def satzende(satz):
    return satz[-1] in satzzeichen

def satzende2(satz):
    return satz[-1] == satzzeichen[0] or satz[-1] == satzzeichen[1] or satz[-1] == satzzeichen[2]


satz1 = "Das ist das Haus vom Nikolaus"
satz2 = "Ich verstehe nicht!"

print(satzende(satz1))
print(satzende(satz2))

print(satzende2(satz1))
print(satzende2(satz2))

from module.konto import Konto

peter = Konto("Peter", 50423)

peter.einzahlen(50)
peter.einzahlen(-5)
peter.abheben(40)
peter.abheben(100)
peter.abheben("Banane")

print(peter)

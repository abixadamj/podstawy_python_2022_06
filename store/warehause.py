class Good:
    model_name = "Personal Computer"

    def __init__(self, our_model, cpu, speed, prod_year):
        """Przeciążenie metody !"""
        print("Hej - jestem init!")
        self.model = our_model
        self.cpu_name = cpu
        self.speed = speed
        self.prod_year = prod_year
        print(f"Utworzyliśmy obiekt ID {id(self)}")

    def opis(self):
        print(f"Jestem {self.model_name} - modelem {self.model}")

    def set_model(self, new_model):
        print(f"Changing model from {self.model} to {new_model}")
        self.model = new_model

    def history(self):
        print(f"Computer {self.model} was born in {self.prod_year}")
        print(f"Was {3400 / self.speed} time slower than today 3400 MHz")


computer_X = Good  # w ten sposób raczej NIE ROBIMY
computer_0 = Good("Komputer XT", "8086", 4, 1990)
computer_1 = Good("Komputer AT", "286", 12, 1993)
computer_2 = Good("Komputer XT/AT", "Pentium/586", 133, 1998)  # poprawne wywołanie tworzenia obiektu
computer_4 = Good("Komputer Adama", "Core i7", 3200, 2020)

computer_1.model = "PC XT"
computer_2.set_model("PC AT Computer")

computer_0.opis()
computer_1.opis()
computer_2.opis()

for comp in (computer_0, computer_1, computer_2, computer_4):
    comp.history()

# print(dir(computer_0))
# print(dir(computer_1))

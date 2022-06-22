class Good:
    CPU_TYPE = None
    model_name = "Personal Computer"

    def __init__(self, our_model):
        """Przeciążenie metody !"""
        print("Hej - jestem init!")
        self.model = our_model
        print(f"Utworzyliśmy obiekt ID {id(self)}")

    def opis(self):
        print(f"Jestem {self.model_name} - modelem {self.model}")

    def set_model(self, new_model):
        print(f"Changing model from {self.model} to {new_model}")
        self.model = new_model


computer_X = Good  # w ten sposób raczej NIE ROBIMY
computer_0 = Good("Komputer XT")
computer_1 = Good("Komputer AT")
computer_2 = Good("Komputer XT/AT")  # poprawne wywołanie tworzenia obiektu

computer_1.model = "PC XT"
computer_2.set_model("PC AT Computer")

computer_0.opis()
computer_1.opis()
computer_2.opis()

# print(dir(computer_0))
# print(dir(computer_1))

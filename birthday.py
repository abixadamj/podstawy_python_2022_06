my_name = input("Podaj mi swoje imię: ")
my_birth = int(input(f"{my_name} - podaj Twój rok urodzenia: "))
actual_year = 2022
my_age = actual_year - my_birth
# F-String
print(f"Siemanko {my_name}, ja jestem Python")
print(f"W roku {actual_year} masz {my_age} lat")

if my_age >= 18:
    print(f"Hej 0 - {my_name} - jesteś {'dorosła' if my_name.endswith('a') else 'dorosły'}")
    print(f'Hej 1 - {my_name} - jesteś {"dorosła" if my_name.endswith("a") else "dorosły"}')

    string_name = "dorosła's" if my_name.endswith("a") else "dorosły"
    print(f"Hej 3 - {my_name} - jesteś {string_name}")

    print(f"Hej 2 - {my_name}")
    if my_name.endswith("a"):
        print("Jesteś kobietą i to dorosłą")
    else:
        print("Jesteś mężczyzną i to dorosłym")
    print("Możesz kupić piwo.")
else:
    print(f"Do dorosłości brakuje ci {18 - my_age} lat.")

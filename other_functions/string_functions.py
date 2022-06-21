def simple_print():
    print("To jest prosta funkcja")


def simple_return():
    print("This is simple return statement...")
    return "ZWRACAMY"


def is_pallindrome(word):
    print(f"Sprawdzam słowo {word}")
    return word == word[::-1]


def simple_bmi(waga, wzrost):
    bmi = waga / wzrost ** 2
    print(f"BMI wynosi {bmi}")
    return bmi


moje_bmi = simple_bmi(73.5, 1.67)
print(f"Wartość {moje_bmi} / typ {type(moje_bmi)}")
if moje_bmi < 20:
    print("Super")
else:
    print("Idź do lekarza")

# is_pallindrome("Adam")
# # print(is_pallindrome("ADAM"))
#
# simple_print()
# wynik = simple_return()
# print(f"Wynik działania to {wynik}")

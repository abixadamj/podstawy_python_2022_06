from payment_functions.read_data import *
from other_functions.finanse_01 import avg_income

our_clients = {}  # słownik — dict
# słownik = { klucz: wartość, klucz1: wartość, klucz2: wartość }

while True:
    client_name = input("Please tell me name of the client (KONIEC aby zakończyć): ")
    if client_name == "KONIEC":
        print("Bye bye ...")
        break

    our_clients[client_name] = read_client_data(client_name)
    print(f"{client_name} data: {our_clients[client_name]}")
    tmp_data = our_clients[client_name]
    income = tmp_data["payments"]
    print(f"Income: {income}")
    tmp_data["next_payment"] = avg_income(income)
    print(f"Values after: {tmp_data}")

# koniec pętli while
print(f"Our full database: {our_clients}")

q = avg_income()

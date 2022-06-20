from payment_functions.read_data import *

our_clients = {}  # słownik — dict
# słownik = { klucz: wartość, klucz1: wartość, klucz2: wartość }

while True:
    client_name = input("Please tell me name of the client (KONIEC aby zakończyć): ")
    if client_name == "KONIEC":
        print("Bye bye ...")
        break

    our_clients[client_name] = read_client_data(client_name)

# koniec pętli while
print(f"Our full database: {our_clients}")

from store.warehause import Good
import pickle

shelf = input("Name of the shelf: ")
shelf_list = []

while True:
    name = input("Computer name (KONIEC):")
    if name == "KONIEC":
        break
    cpu = input("CPU: ")
    speed = int(input("Speed (MHz): "))
    prod_year = int(input("Production year: "))
    computer = Good(name, cpu, speed, prod_year)
    shelf_list.append(computer)

if shelf_list:
    print("OK")
    our_store_db = {shelf: shelf_list}
    with open("dbstore.dat", "wb") as dbfile:
        try:
            pickle.dump(our_store_db, dbfile)
            print("Done")
        except:
            print("Error")

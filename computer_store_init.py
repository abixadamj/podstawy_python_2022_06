from store.warehause import Good
from store.db_write import *
import sys

shelf = input("Name of the shelf: ")
shelf_list = []
our_store = {
    "shelf": [Good("AT", "i7", 2200, 2020),
              Good("AT", "i7Mobile", 1800, 2017),
              Good("XT", "8086", 7, 1994)],
    "backoffice": [Good("MSX", "Z80", 4, 1984),
                   Good("Commodore", "Z80", 4, "1985")]
}

while True:
    name = input("Computer name (KONIEC|PREP):")
    if name == "PREP":
        pickle_write_data(our_store, "db2.dat")
        # ustawimy exit code na 118
        sys.exit(118)
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
    pickle_write_data(our_store_db)

from store.warehause import Good

shelf = input("Name of the shelf: ")

while True:
    shelf_list = []
    name = input("Computer name (KONIEC):")
    if name == "KONIEC":
        break
    cpu = input("CPU: ")
    speed = int(input("Speed (MHz): "))
    prod_year = int(input("Production year: "))
    computer = Good(name, cpu, speed, prod_year)
    shelf_list.append(computer)

if shelf_list:
    our_store_db = {shelf, shelf_list}

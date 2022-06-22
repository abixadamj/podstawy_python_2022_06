from store.warehause import Good

our_store = {
    "shelf": [Good("AT", "i7", 2200, 2020),
              Good("AT", "i7Mobile", 1800, 2017),
              Good("XT", "8086", 7, 1994)],
    "backoffice": [Good("MSX", "Z80", 4, 1984),
                   Good("Commodore", "Z80", 4, "1985")]
}

if __name__ == "__main__":
    print('OUR STORE!')

import pickle


def pickle_write_data(database, file_name="dbstore.dat"):
    with open(file_name, "wb") as dbfile:
        try:
            pickle.dump(database, dbfile)
            return True
        except:
            return False

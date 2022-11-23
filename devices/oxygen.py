from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("oxygen", 75 + random() * 30, "oxygen_1")
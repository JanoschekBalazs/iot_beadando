from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("oxygen", 90 + random() * 10, "oxygen_1")
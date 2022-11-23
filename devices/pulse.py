from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("pulse", 110 + random() * 10, "pulse_1")
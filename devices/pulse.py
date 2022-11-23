from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("pulse", 40 + random() * 200, "pulse_1")
from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("body_heat", 33 + random() * 6, "body_heat_1")
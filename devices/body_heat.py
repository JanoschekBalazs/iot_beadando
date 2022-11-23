from random import random
from devices import data_supplier

def supplier():
    return data_supplier.supply("body heat", 36 + random() * 3, "body_heat_1")
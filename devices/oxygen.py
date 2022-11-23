from random import random
from devices import data_supplier
from weight_magnet_controller import weight

def supplier():
    return data_supplier.supply("oxygen", (75 + random() * 30) - weight/10, "oxygen_1")
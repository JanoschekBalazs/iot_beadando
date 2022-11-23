from random import random
from devices import data_supplier
from weight_magnet_controller import weight

def supplier():
    return data_supplier.supply("pulse", (40 + random() * 200 + weight/2), "pulse_1")
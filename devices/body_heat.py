from random import random
from devices import data_supplier
from weight_magnet_controller import weight

def supplier():
    return data_supplier.supply("body_heat", (33 + random() * 6) + weight/50, "body_heat_1")
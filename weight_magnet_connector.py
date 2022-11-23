import mqtt_client as mqtt
from devices import data_supplier
from weight_magnet_controller import weight

def supplier():
    return data_supplier.supply("weight", weight, "weight_magnet")

mqtt.connect_telemetry(supplier)
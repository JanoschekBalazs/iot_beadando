import mqtt_client as mqtt
from devices import oxygen

mqtt.connect_device(oxygen.supplier)
import mqtt_client as mqtt
from devices import body_heat

mqtt.connect_device(body_heat.supplier)
import mqtt_client as mqtt
from devices import body_heat

mqtt.connect_telemetry(body_heat.supplier)
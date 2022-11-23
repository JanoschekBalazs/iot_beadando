import mqtt_client as mqtt
from devices import oxygen

mqtt.connect_telemetry(oxygen.supplier)
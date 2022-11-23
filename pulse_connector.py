import mqtt_client as mqtt
from devices import pulse

mqtt.connect_telemetry(pulse.supplier)
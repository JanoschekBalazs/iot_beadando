import paho.mqtt.client as mqtt
import threading

def connect_telemetry(data_supplier):

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    def send():
        data = data_supplier()
        print("Data sent: " + str(data))
        client.publish("v1/devices/me/telemetry", "{\"" + str(data.get("metric")) +"\":" + str(data.get("payload")) + "}")
        threading.Timer(1, send).start()

    def on_connect(client, userdata, flags, rc):
        print("Connected to the broker with the following code: "+str(rc))
        threading.Timer(1, send).start()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(data_supplier().get("token"), "")
    client.connect("127.0.0.1", 1883, 60)
    client.loop_forever()

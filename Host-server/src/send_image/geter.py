import sys
sys.path.append('/home/denis7502/src/sasha')
from client import Client
from paho.mqtt import client as mqtt_client
import cv2
import numpy as np

class getImage(Client):
    def __init__(self, broker, port, topic, q=None ) -> None:
        super().__init__(broker, port, topic, q)
        self.client_id = f'python-mqtt-{3}'
        self.frame = np.zeros((480,480,3))

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print(f"Connected to MQTT Broker! {self.topic}")
            else:
                print("Failed to connect, return code %d\n", rc)
        # Set Connecting Client ID
        client = mqtt_client.Client(self.client_id)
        #client.username_pw_set(username, password)
        client.on_connect = on_connect
        client.connect(self.broker, self.port)
        return client

    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            #img = msg.payload
            nparr = np.frombuffer(msg.payload, np.uint8)
            try:
                self.frame = nparr.reshape((480,480))
            except:
                self.frame = nparr.reshape((480,480,3))

        client.subscribe(self.topic)
        client.on_message = on_message
    
    def run_subscribe(self):
        self.client = self.connect_mqtt()
        self.client.loop_start()
        self.subscribe(self.client)

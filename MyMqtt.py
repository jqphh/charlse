#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import paho.mqtt.client as mqtt    


class MyMqttClient:
    client = None
    mqttHost = None
    mqttPort = 0
    mqttClientSn = None
    mqttHeartbeat = 0
    on_connect     = None
    on_disconnect  = None
    on_message     = None
    on_publish     = None
    
    def __init__(self, host, sn, port=1883, heartbeat=30):
        self.mqttHost = host
        self.mqttPort = port
        self.mqttClientSn = sn
        self.mqttHeartbeat = heartbeat

    def mqtt_start(self):
        clientId = "d:" + self.mqttClientSn
        self.client = mqtt.Client(clientId)
        self.client.on_connect = self.on_connect
        self.client.on_disconnect = self.on_disconnect
        self.client.on_publish = self.on_publish
        self.client.on_message = self.on_message
        username = "IPP:d:" + self.mqttClientSn
        # client.username_pw_set(username, "")
        self.client.connect(self.mqttHost, self.mqttPort, self.mqttHeartbeat)
        self.client.loop_forever()

    def mqtt_close(self):
        self.client.disconnect()
        
    def mqtt_send(self, topic, payload):
        self.client.publish(topic, payload, 1, False)

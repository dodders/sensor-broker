import paho.mqtt.client as mqtt
import pymongo as mongodb
import Database
import datetime
import ptvsd
ptvsd.enable_attach('llyr24_debug')

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
  mqttclient.subscribe("/GDESGW1/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
  print("Topic: " + msg.topic + "\nMessage: " + str(msg.payload))
  elements = msg.topic.split('/')
  
  if (len(elements) == 6):
      db.Sensors.insert_one(
          {
            "model":elements[1],
            "gateway_id":elements[2],
            "node_id":elements[3],
            "type":elements[4],
            "value": str(msg.payload),
            "time": datetime.datetime.timestamp(datetime.datetime.now())
          })


  #db.Insert(msg.topic, msg.payload)



#db = Database.Database()

mongoclient = mongodb.MongoClient("mongodb://localhost:27017/")
db = mongoclient.gdtechdb_test



mqttclient = mqtt.Client()
mqttclient.on_connect = on_connect
mqttclient.on_message = on_message

mqttclient.connect("74.208.159.205", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
mqttclient.loop_forever()

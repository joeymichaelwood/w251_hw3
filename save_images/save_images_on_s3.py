import paho.mqtt.client as mqtt
import boto3
import uuid

LOCAL_MQTT_HOST="mosquitto-service""
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mosquitto_face"

client = boto3.client('s3')

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def store_image(img):
    s3.put_object(
        Bucket='berkeley-251',
        Body=img,
        Key=str(uuid.uuid4()),
        ACL='public-read',
        ContentType='image/png'
    )


def on_message(client,userdata, msg):
  try:
    msg = msg.payload
    store_image(msg)
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message
local_mqttclient.loop_forever()
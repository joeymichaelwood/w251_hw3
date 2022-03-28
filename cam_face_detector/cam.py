import sys
import cv2 as cv
import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="mosquitto_face"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

# # def on_message(client,userdata, msg):
# #   try:
# #     print("message received: ",str(msg.payload.decode("utf-8")))
# #     # if we wanted to re-publish this message, something like this should work
# #     # msg = msg.payload
# #     # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
# #   except:
# #     print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.loop_start()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
# local_mqttclient.on_message = on_message

cam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cam.read()

    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for face_details in faces:
        (x, y, w, h) = face_details
        y_height = y + h
        x_width = x + w
        face = gray[y: y_height, x: x_width]

        _, pic = cv.imencode('.png', face)
        local_mqttclient.publish(LOCAL_MQTT_TOPIC, payload=pic.tobytes(), qos=0, retain=False)

    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
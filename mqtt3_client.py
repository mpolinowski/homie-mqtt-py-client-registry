import json, sys, time
from paho.mqtt import client as mqtt_client
# Import MQTT Broker configuration from config.py
from config import *

f = open(mqtt_device_config)
json_array = json.load(f)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("INFO :: Homie device configured")
        client.subscribe(mqtt_homie_prefix)
    else:
        print("ERROR :: Connection failed: {rc}".format(rc=rc), )


def on_message(client, userdata, msg):
    # print("INFO :: Received `{payload}` from `{topic}`".format(
    #     payload=msg.payload.decode(), topic=msg.topic))

    if (msg.topic == 'homie/homie_device/alarm/alarm-armed/set'):
        client.publish("{prefix}alarm/actions/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm/alarm-email/set'):
        client.publish("{prefix}alarm/actions/email/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm/pir/set'):
        client.publish("{prefix}alarm/actions/pir/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm/pir-link/set'):
        client.publish("{prefix}alarm/actions/pir/link/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm/alarm-trigger/set'):
        client.publish("{prefix}alarm/pushalarm/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm/audio-detection/set'):
        client.publish("{prefix}alarm/actions/audiodetection/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/red-enabled/set'):
        client.publish("{prefix}alarm/areas/red/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/blue-enabled/set'):
        client.publish("{prefix}alarm/areas/blue/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/green-enabled/set'):
        client.publish("{prefix}alarm/areas/green/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/yellow-enabled/set'):
        client.publish("{prefix}alarm/areas/yellow/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/red-sense/set'):
        client.publish("{prefix}alarm/areas/red/sensitivity/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/blue-sense/set'):
        client.publish("{prefix}alarm/areas/blue/sensitivity/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/green-sense/set'):
        client.publish("{prefix}alarm/areas/green/sensitivity/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/alarm-areas/yellow-sense/set'):
        client.publish("{prefix}alarm/areas/yellow/sensitivity/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/audio-out/set'):
        client.publish("{prefix}multimedia/audio/out/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/audio-in/set'):
        client.publish("{prefix}multimedia/audio/in/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/auto-gamma/set'):
        client.publish("{prefix}multimedia/image/gamma/auto/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/gamma/set'):
        client.publish("{prefix}multimedia/image/gamma/preset/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/auto-denoise/set'):
        client.publish("{prefix}multimedia/image/denoise/auto/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/denoise/set'):
        client.publish("{prefix}multimedia/image/denoise/preset/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/flip/set'):
        client.publish("{prefix}multimedia/image/transform/flip/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/mirror/set'):
        client.publish("{prefix}multimedia/image/transform/mirror/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/brightness/set'):
        client.publish("{prefix}multimedia/image/brightness/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/contrast/set'):
        client.publish("{prefix}multimedia/image/contrast/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/saturation/set'):
        client.publish("{prefix}multimedia/image/saturation/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/hue/set'):
        client.publish("{prefix}multimedia/image/hue/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/sharpness/set'):
        client.publish("{prefix}multimedia/image/sharpness/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/vibrancy/set'):
        client.publish("{prefix}multimedia/image/vibrancy/value/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/multimedia/isomax/set'):
        client.publish("{prefix}multimedia/image/isomax/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/system/reboot/set'):
        client.publish("{prefix}system/reboot/now/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/system/autoled/set'):
        client.publish("{prefix}features/nightvision/autoled/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/system/autoircut/set'):
        client.publish("{prefix}features/nightvision/autoircut/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/privacy/mask1/set'):
        client.publish("{prefix}multimedia/privacy/region1/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/privacy/mask2/set'):
        client.publish("{prefix}multimedia/privacy/region2/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/privacy/mask3/set'):
        client.publish("{prefix}multimedia/privacy/region3/enable".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    elif(msg.topic == 'homie/homie_device/privacy/mask4/set'):
        client.publish("{prefix}multimedia/privacy/region4/enable/raw".format(prefix=mqtt_camera_prefix), msg.payload.decode())
    else:
        # print("WARNING :: Unrecognized MQTT Topic `{topic}`".format(topic=msg.topic))
        return

    


def connect_mqtt():
    client = mqtt_client.Client(client_id = mqtt_client_id)
    client.username_pw_set(username = mqtt_username, password = mqtt_password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host = mqtt_server_host, port = mqtt_server_port)
    # publish configuration updates
    for entity in json_array['entities']:
        client.publish(entity['topic'],entity['payload'],retain=True)
        time.sleep(0.100)
    f.close()
    return client


def run():
    client = connect_mqtt()
    client.loop_forever()


if __name__ == '__main__':
    run()

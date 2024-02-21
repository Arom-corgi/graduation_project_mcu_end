# simple是MQTT库的一部分，连接阿里云用到它
from simple import MQTTClient
import wifi
from config import aliyun_config


def connect_aliyun():
    wifi.do_connect()
    # 配置MQTT客户端连接参数
    clientId = aliyun_config["clientId"]
    mqttHostUrl = aliyun_config["mqttHostUrl"]
    port = aliyun_config["port"]
    username = aliyun_config["username"]
    passwd = aliyun_config["passwd"]
    # 创建MQTT客户端
    client = MQTTClient(client_id=clientId, server=mqttHostUrl, port=port, user=username, password=passwd, keepalive=60)
    # 连接到服务器
    try:
        client.connect()
        print("MQTT客户端已连接到阿里云物联网平台")
        # 定义要发布的Topic和消息内容
        topic = '/sys/{}/{}/thing/event/property/post'.format(aliyun_config["ProductKey"], aliyun_config["DeviceName"])
        # 示例：上传心率数据
        payload = '{"params": {"heart_rate": 65}}'
        # 发布消息
        client.publish(topic, payload)
    except Exception as e:
        print("连接失败：", e)
connect_aliyun()
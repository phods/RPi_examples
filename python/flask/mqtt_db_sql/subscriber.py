import sys
import paho.mqtt.client as mqtt
import sqlite3

broker = "test.mosquitto.org"
port = 1883
keppAlive = 60
topic = 'DZ/#'

# funcao responsavel por cadastrar no banco de dados a temperatura do sensor
def insertTemperature(message):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO temperature
        (temperature)
        VALUES (?)
    """, (message,))

    conn.commit()
    conn.close()

def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))

    client.subscribe(topic)

def on_message(client, userdata, msg):

    message = str(msg.payload) # converte a mensagem recebida
    print("[MSG RECEBIDA] Topico: "+msg.topic+" / Mensagem: "+ message)

    if msg.topic == 'DZ/gauge/temperature':

        insertTemperature(message) # invoca o metodo de cadastro passando por parametro a temperatura recebida

try:
    print("[STATUS] Inicializando MQTT...")

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker, port, keppAlive)
    client.loop_forever()

except KeyboardInterrupt:
    print ("\nScript finalizado.")
    sys.exit(0)

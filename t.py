from POOcom import ClientCom
from time import sleep

client = ClientCom()

@client.on_message
def new(msg):
    print(f"-> {msg}")

for x in range(10):
    client.send(x)

sleep(2)
client.close()
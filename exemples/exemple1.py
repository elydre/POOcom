# on import le module costom
from POOcom import ClientCom

client = ClientCom(channel="test")

# on définit une fonction qui sera appelée lorsqu'on reçoit un message
@client.on_message
def new(channel, msg):
    print(f"<{channel}> {msg}")

while True:
    # on envoie un msg
    client.send(input())
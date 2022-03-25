# on import le module costom
from POOcom import ClientCom

client = ClientCom()

# on définit une fonction qui sera appelée lorsqu'on reçoit un message
@client.on_message
def new(msg):
    print(f"-> {msg}")

while True:
    # on envoie un msg
    client.send(input())
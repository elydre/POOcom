# on import le module costom
from POOcom import ClientCom

# fonction pour affichier un msg
def new_msg(channel, msg):
    print(f"<{channel}> {msg}")

# on crée un objet client
client = ClientCom(channel="test")

# on map la fonction new_msg pour qu'elle soit appelée lorsqu'on reçoit un msg
client.map(new_msg)

while True:
    # on envoie un msg
    client.send(input())
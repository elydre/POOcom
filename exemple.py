# on import le module POOcom
from POOcom import ClientCom

client = ClientCom()
print("init done!")

# on définit une fonction qui sera
# appelée qu'un message est reçu
@client.on_message
def new(msg):
    print(f"-> {msg}")

while True:
    # on envoie un msg
    client.send(input())

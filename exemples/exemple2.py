from POOcom import ClientCom

# on crée un objet client
client = ClientCom(channel="test")

# on définit une fonction qui sera appelée lorsqu'on reçoit un message
@client.on_message
def all_channel(channel, msg):
    print(f"<{channel}> {msg}")

print("channel <entrer>\nmessage <entrer>")
while True:
    # on envoie un msg
    client.send(channel = input(), msg = input())
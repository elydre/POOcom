# Introduction

com-server est une platforme de communication client-serveur avec serveur pré-hebergé.

## Installation

Télécharger POOcom.py et placez le dans le dossier de votre projet.

# Usage

## importation du module
```py
from POOcom import ClientCom
```

## création du client
```py
# simple:
client = ClientCom("channel_name")

# aprofondi:
client = ClientCom(channel = "channel_name", host = "pf4.ddns.net", port = 63535)
```


## envoie de messages

**channel** et le channel dans lequel le message est envoyé ou **True** pour le channel par défaut.
```py
# simple:
client.send("message")

# aprofondi:
client.send(msg = "message", channel = "channel_name")
```

## réception de messages

### decorateur
pour que la fonction soit appelée lorsque le message est reçu, il faut utiliser le decorateur `on_message`
```py
@client.on_message
```

### création d'une fonction de reception
le decorateur `on_message` peux prendre `only_channel` (bool) pour ne recevoir que les messages dans le channel spécifié.

la fonction doit prendre 2 arguments:
- la channel du message
- le message

```py
@client.on_message(only_channel=False)
def only_channel(channel, msg):
    print(f"<{channel}> {msg}")
```
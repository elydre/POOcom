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


## envoie de message

**channel** et le channel dans lequel le message est envoyé ou **True** pour le channel par défaut.
```py
# simple:
client.send("message")

# aprofondi:
client.send(msg = "message", channel = "channel_name")
```

## réception de message

### création d'une fonction de reception
la fonction doit prendre 2 arguments:
- la channel du message
- le message

```py
def new_msg(channel, msg):
    print(f"<{channel}> {msg}")
```

### mapping de la fonction

**map** et la fonction a relier
**only_channel** et du seul channel qui peut afficher des messages ou **True** pour le channel par défaut et **False** pour tous les channels
```py
# simple:
client.map(new_msg)

# aprofondi:
client.map(map = new_msg, only_channel = "channel_name")
```
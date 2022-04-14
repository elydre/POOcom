# Introduction

com-server est une platforme de communication client-serveur avec serveur pré-hebergé.

## Installation

Téléchargez POOcom.py et placez le dans le dossier de votre projet.

# Usage

## importation du module
```py
from POOcom import ClientCom
```

## création du client
```py
# simple:
client = ClientCom()

# aprofondi:
client = ClientCom(host = "pf4.ddns.net", port = 63535)
```

## envoie de messages

```py
client.send("As-tu déjà dansé avec le diable au clair de lune ?")
```

## réception de messages

### decorateur
pour que la fonction soit appelée lorsque le message est reçu, il faut utiliser le decorateur `on_message`
```py
@client.on_message
```

### création d'une fonction de reception

la fonction doit prendre en argument le message reçu:

```py
@client.on_message
def only_channel(msg):
    print(f"-> {msg}")
```
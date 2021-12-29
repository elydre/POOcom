'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
 - codé en : UTF-8
 - langage : python 3
 - GitHub  : github.com/pf4-DEV
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

import socket
from _thread import start_new_thread

version = "0.2.5"

def recv_msg(s,map, only_channel):
    while True:
        msg = s.recv(1024).decode()
        msg_channel = msg.split('§')[0] if len(msg.split('§')[0]) > 1 else None
        msg = msg if msg_channel is None else "".join(msg.split('§')[1:])
        if only_channel in [msg_channel, False]:
            map(msg_channel, msg)

class ClientCom:
    def __init__(self,channel = "general", host = "pf4.ddns.net", port = 63535):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        self.channel = channel

    def change_channel(self, channel):
        self.channel = channel     

    def on_message(self, fonction):
        if fonction.__name__ == "only_channel":
            start_new_thread(recv_msg, (self.s, fonction.__call__ , self.channel))
        elif fonction.__name__ == "all_channel":
            start_new_thread(recv_msg, (self.s, fonction.__call__ , False))
        else:
            print(f"[POOcom] Erreur : nom de fonction invalide -> '{fonction.__name__}' (only_channel/all_channel)")
        return fonction
    

    def send(self, msg, channel = True):
        if str(channel) == "True": channel = self.channel
        self.s.send(f"{channel}§{msg}".encode())

    def close(self):
        self.s.close()
'''    _             _
  ___ | | _   _   __| | _ __   ___
 / _ \| || | | | / _` || '__| / _ |
|  __/| || |_| || (_| || |   |  __/
 \___||_| \__, | \__,_||_|    \___|
          |___/
___________________________________

 - codé en : UTF-8
 - langage : python3
 - GitHub  : github.com/elydre
 - Licence : GNU GPL v3
'''

from time import sleep
from urllib.request import Request, urlopen
import socket
from _thread import start_new_thread
import json

HOST = "192.168.1.100"
PORT = 63535

WEBHOOK_URL = "webhooks url"  # change this
USE_WEBHOOK = False

liste_conn = []
ban = []

stat = {
    "msg_send": 0,
    "msg_recv": 0,
}

dis_print = lambda msg: urlopen(Request(
            WEBHOOK_URL,
            data=json.dumps({
                'content': msg}).encode(),
            headers={
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            })) if USE_WEBHOOK else print(msg)

def send_print():
    while True:
        if len(liste_conn) > 0 or stat["msg_send"] > 0:
            msg = "**- STAT -**\n```\n"
            msg += f"\n- in msg/sec  : {round(stat['msg_recv'] / 60, 2)}"
            msg += f"\n- out msg/sec : {round(stat['msg_send'] / 60, 2)}"
            msg += f"\n- clients     : {len(liste_conn)}"
            msg += f"\n- ban         : {len(ban)}"
            msg += "\n```\n"
            msg = msg[:500]+'\n...' if len(msg) > 500 else msg
            dis_print(msg)

        stat['msg_recv'] = 0
        stat['msg_send'] = 0

        sleep(60)


def send_all(data):
    stat['msg_recv'] += 1
    for conn in liste_conn:
        stat['msg_send'] += 1
        conn[0].sendall(data.encode())


def echange(conn, addr):
    if addr[0] in ban:
        dis_print(f"{addr[0]} - BANNED")
        conn.close()
        return
    with conn:
        dis_print(f"**{addr[0]}~{addr[1]} c'est connecte!**")
        liste_conn.append([conn, addr])
        while True:
            try:
                if data := conn.recv(1024):
                    send_all(data.decode())
                else:
                    break
            except Exception:
                conn.close()
                break
    liste_conn.remove([conn, addr])
    dis_print(f"**{addr[0]}~{addr[1]} c'est déconnecte**")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    dis_print("**Socket créé**")
    s.listen()
    start_new_thread(send_print, ())
    while True:
        dis_print("Attente de connexion...")
        conn, addr = s.accept()
        start_new_thread(echange, (conn, addr))

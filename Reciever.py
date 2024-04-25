import socket
import os
import subprocess
from time import sleep
from tkinter.messagebox import showerror, showwarning, showinfo
##import tkinter as tk
##
##root = tk.Tk()

def CommandSplit(st):
    if len(st) == 0: return ("", [])
    command = ""
    i = 0
    while st[i] != ' ':
        command += st[i]
        i += 1
        if (i > len(st) - 1): break
    arguments = []
    cur = ""
    stat = False
    for b in range(i + 1, len(st)):
        if (st[b] == '"'): stat = not(stat)
        if (stat and st[b] != '"'): cur += st[b]
        if not(stat) and len(cur) != 0:
            arguments.append(cur)
            cur = ""
    return (command, arguments)

def AcceptCommand(command):
    cmd, arg = CommandSplit(command)
    if (cmd == 'print' and len(arg) > 0):
        print(arg[0])
        return "print successful"
    f = open("1.txt", "w").close()
    result = os.system(command + f' >> 1.txt')
    if result == 0:
        back_message = open('1.txt').readline().replace('\n', '')
        if back_message != '': return back_message
        else: return "executed successful"
    else: return "хуйню сморозил"
        
command = ['b']
while command[0] != 'stop':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    while command[0] != 'stop':
        try: command = bytes.decode(conn.recv(1024))
        except: break
        back_message = AcceptCommand(command)
        conn.send(str.encode(back_message))
    print("ERROR: socket disconected")

# curlengh = 0
# filename = ''
# filelengh = ''
# stage = 0
# f = 0

# while True:
#     n = conn.recv(1)
#     if (stage == 0 and n != b'#'): filename += bytes.decode(n)
#     if (stage == 1 and n != b'%'): filelengh += bytes.decode(n)
#     if (stage == 2):
#         f.write(n)
#         curlengh += 1
#     if (n == b'#' and stage == 0):
#         f = open('new_' + filename, 'wb')
#         stage += 1
#     if (n == b'%' and stage == 1):
#         filelengh = int(filelengh)
#         stage += 1
#     if (stage == 2):
#         if (curlengh >= filelengh):
#             f.close()
#             break

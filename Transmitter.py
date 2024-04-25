import socket
import os
from time import sleep

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'

running = True

os.system("cls")
print(f'{yellow}Searching reciever in local network...')
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 9090))
    except:
        print(f'{red}Reciever does not exist. Trying again.')
        sleep(1)
        continue
    else: break
print(f'{green}Socket created')

command = ''
while command != 'stop':
    command = input()
    sock.send(str.encode(command))
    back_message = bytes.decode(sock.recv(1024))
    print(back_message)
sock.close()

##f = 0
##fr = 0
##
##while running:
##    #os.system("cls")
##    while True:
##        filename = input(f'{yellow}Path to file:')
##        if (filename == 'exit'): running = False
##        try: f = open(filename, 'rb')
##        except: print(f'{red}Wrong filename')
##        else:
##            fr = str(os.path.getsize(filename))
##            break
##    if not(running): break
##    print(f'{green}Filename accepted')
##    sock.send(str.encode(filename.split('/')[-1] + '#'))
##    sock.send(str.encode(fr + '%'))
##    buf = '1'
##    while (buf != b''):
##        buf = f.read(1024)
##        sock.send(buf)
##    print(f'{green}Transmission finished!')

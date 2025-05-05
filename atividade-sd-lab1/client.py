from socket import *
from constCS import *
import threading
import time

def make_request(command):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(command.encode())
    response = s.recv(1024).decode()
    print(f"Resposta para '{command}':\n{response}")
    s.close()

import time

comandos = []
qtd = int(input("Quantas requisições deseja enviar simultaneamente? "))

for i in range(qtd):
    cmd = input(f"Digite o comando {i+1} (ADD <nome> <número>, UPDATE <nome> <novo_número>, LIST): ")
    comandos.append(cmd)

inicio = time.time()

threads = []
for cmd in comandos:
    t = threading.Thread(target=make_request, args=(cmd,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

fim = time.time()
print(f"\nTempo total de execução: {fim - inicio:.2f} segundos")

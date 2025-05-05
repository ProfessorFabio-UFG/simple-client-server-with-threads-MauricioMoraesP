from socket import *
from constCS import *
import threading
import time

phone_book = {}

def handle_client(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        time.sleep(2)  # Simula tempo de processamento
        if data.startswith("ADD"):
            parts = data.split(" ")
            if len(parts) != 3:
                conn.send("Formato inválido. Use: ADD <nome> <número>".encode())
                continue
            name, number = parts[1], parts[2]
            phone_book[name] = number
            conn.send(f"Contato {name}: {number} adicionado.".encode())

        elif data.startswith("UPDATE"):
            parts = data.split(" ")
            if len(parts) != 3:
                conn.send("Formato inválido. Use: UPDATE <nome> <novo_número>".encode())
                continue
            name, new_number = parts[1], parts[2]
            if name in phone_book:
                phone_book[name] = new_number
                conn.send(f"Contato {name} atualizado.".encode())
            else:
                conn.send(f"Contato {name} não encontrado.".encode())

        elif data == "LIST":
            if not phone_book:
                conn.send("Agenda vazia.".encode())
            else:
                contacts = "\n".join(f"{n}: {num}" for n, num in phone_book.items())
                conn.send(f"Contatos:\n{contacts}".encode())
        else:
            conn.send("Comando inválido.".encode())
    conn.close()

def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    print(f"[SERVIDOR INICIADO] Aguardando conexões em {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    main()

import socket

# Sunucu IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 65432

# Soket oluşturma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    # Bağlantıyı kabul etme
    conn, addr = s.accept()
    with conn:
        print('Bağlantı adresi:', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Alınan mesaj:', data.decode())
            conn.sendall(data)

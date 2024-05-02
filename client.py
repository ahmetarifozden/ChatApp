import socket

# Sunucu IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 65432

# Soket oluşturma ve sunucuya bağlanma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Kullanıcıdan mesaj alıp sunucuya gönderme
        message = input("Mesajınızı girin: ")
        s.sendall(message.encode())

        # Sunucudan gelen cevabı alma
        data = s.recv(1024)
        print('Sunucudan gelen cevap:', data.decode())

import socket
import os

def main():
    # filename = 'file_to_send.txt'
    # filename = '2Kc75rfp4xE.jpg'
    # filename = '4k.mp4'
    host = '127.0.0.1'
    port = 8000
    buf = 1024
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print('listening')
    client, address = server.accept()
    print(f'{address} connected')
    filename = client.recv(buf).decode()
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            data = file.read()
            client.sendall(data)
    else:
        client.sendall(b'\x00')
    client.close()
    print(f'{address} closed')
    server.close()
    print('server closed')


if __name__ == '__main__':
    main()

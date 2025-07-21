import socket
import ssl


def main():
    host = '127.0.0.1'
    port = 8000
    buf = 1024
    context = ssl.create_default_context()
    client = socket.create_connection((host, port))
    secure_client = context.wrap_socket(client, server_hostname=host)
    print('connected')
    filename = 'file_to_send.txt'
    filename = filename.replace('../', '')
    secure_client.sendall(filename.encode())
    filename = 'received_' + filename
    with open(filename, 'wb') as file:
        data = secure_client.recv(buf)
        if data == b'\x00':
            print('file does not exist')
            data = ''
        while data:
            file.write(data)
            data = secure_client.recv(buf)
    secure_client.close()
    client.close()
    print('client closed')


if __name__ == '__main__':
    main()

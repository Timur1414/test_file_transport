import socket

def main():
    host = '127.0.0.1'
    port = 8000
    buf = 1024
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    print('connected')
    filename = 'file_to_send.txt'
    # filename = '2Kc75rfp4xE.jpg'
    # filename = '4k.mp4'
    # filename = 'server.py'
    # filename = 'ser1ver.py'
    # filename = 'C:/Users/timat/.gitconfig'
    filename = filename.replace('../', '')
    client.sendall(filename.encode())
    filename = 'received_' + filename
    with open(filename, 'wb') as file:
        data = client.recv(buf)
        if data == b'\x00':
            print('file does not exist')
            data = ''
        while data:
            file.write(data)
            data = client.recv(buf)
    client.close()
    print('client closed')


if __name__ == '__main__':
    main()

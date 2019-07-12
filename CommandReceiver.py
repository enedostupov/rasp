import threading
import socket


class CommandReceiver(threading.Thread):
    def __init__(self, ip, port, length, serial_port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.packet_length = length
        self.serial_port = serial_port

    def run(self):
        sock = socket.socket()
        sock.bind((self.ip, self.port))
        sock.listen(1)
        while True:
            print('[CommandReceiver] waiting for connection... ')
            connection, address = sock.accept()
            print('[CommandReceiver] has connection: ', address)
            while True:
                try:
                    data = connection.recv(self.packet_length)
                    if not data:
                        continue

                    packet = data.decode('utf-8')

                    if packet[0] == '9':
                        print('[CommandReceiver] closing connection...')
                        break
                    self.serial_port.write(packet)
                    print(packet)
                except socket.error as e:
                    print('[CommandReceiver] error receiving command', e)
                    break
            connection.close()

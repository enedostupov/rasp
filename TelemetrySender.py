import threading
import time


class TelemetrySender(threading.Thread):
    def __init__(self, ip, port, length, serial_port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.packet_length = length
        self.serial_port = serial_port

    def run(self):
        while True:
            response = self.serial_port.readline().rstrip()
            print(response)

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
            response = ''
            time.sleep(1)
            while self.serial_port.inWaiting() > 0:
                next_char = self.serial_port.read(1)
                if next_char == '#':
                    break
                response += next_char;
            print(response)

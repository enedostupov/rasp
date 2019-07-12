import os
import serial
import time


class SerialInitializer:
    def __init__(self, request):
        self.ports = {}
        self.request = request
        self.path = '/dev'
        self.fill_up_enabled_ports()

    def is_port_enabled(self, port_name):
        full_port_name = self.path + '/' + port_name
        ser = serial.Serial()
        ser.port = full_port_name
        ser.baudrate = 9600
        try:
            ser.open()
            ser.write(self.request)
        except:
            return
        response = ''
        time.sleep(1)
        while ser.inWaiting() > 0:
            response += ser.read(1)
        self.ports[response] = full_port_name
        ser.close()

    def fill_up_enabled_ports(self):
        dirs = os.listdir(self.path)
        for file in dirs:
            self.is_port_enabled(file)

    def get_port_by_response(self, response):
        if response in self.ports:
            return self.ports[response]
        return None

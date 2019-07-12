import os
import serial
import time
import re


class SerialInitializer:
    def __init__(self, request):
        self.ports = {}
        self.request = request
        self.path = '/dev'
        self.mask = 'ttyUSB'
        self.fill_up_enabled_ports()

    def is_port_enabled(self, port_name):
        full_port_name = self.path + '/' + port_name
        print(full_port_name)
        try:
            ser = serial.Serial(full_port_name, 9600)
        except:
            print('can not open serial')
            return

        try:
            ser.write(self.request)
        except:
            print('can not write')

        response = ''
        time.sleep(1)
        while ser.inWaiting() > 0:
            response += ser.read(1)
        print(response)
        self.ports[response] = full_port_name
        ser.close()

    def fill_up_enabled_ports(self):
        dirs = os.listdir(self.path)
        for file in dirs:
            if re.match(self.mask, file):
                self.is_port_enabled(file)

    def get_port_by_response(self, response):
        if response in self.ports:
            return self.ports[response]
        return None

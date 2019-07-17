import os
import serial
import time
import re


class SerialInitializer:
    def __init__(self, request, serial_speed):
        self.ports = {}
        self.request = request
        self.path = '/dev'
        self.mask = 'ttyUSB'
        self.serial_speed = serial_speed
        self.fill_up_enabled_ports()
        for key in self.ports:
            print( key + ' = ' + self.ports[key] )

    def is_port_enabled(self, port_name):
        full_port_name = self.path + '/' + port_name
        print(full_port_name)
        ser = serial.Serial()
        ser.port = full_port_name;
        ser.baudrate = self.serial_speed
        ser.timeout = 10
        try:
            ser.open()
        except:
            print('can not open serial')
            return
        try:
            ser.write(self.request)
        except:
            print('can not write')
        response = ser.readline().rstrip() 
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

from SerialInitializer import SerialInitializer
from TelemetrySender import TelemetrySender

import serial
import time

serial_speed = 9600

serialInitializer = SerialInitializer('900000#', serial_speed)
print('SerialInitializer - done')


commandReceiver = None
control_response = '900001#'
control_port = 6001
control_serial_device_name = serialInitializer.get_port_by_response(control_response)
if control_serial_device_name:
    print('control port was founded' + control_serial_device_name)
    control_serial = serial.Serial(control_serial_device_name, serial_speed)
    commandReceiver = CommandReceiver('', control_port, 7, control_serial)
    commandReceiver.start()
else:
    print('control port was NOT founded')

telemetrySender = None
telemetry_response = '900002#'
telemetry_port = 6001
telemetry_serial_device_name = serialInitializer.get_port_by_response(telemetry_response)
if telemetry_serial_device_name:
    print('telemetry port was founded')
    telemetry_serial = serial.Serial(telemetry_serial_device_name, serial_speed)
    telemetrySender = TelemetrySender('', telemetry_port, 7, telemetry_serial)
    telemetrySender.start()
else:
    print('telemetry port was NOT founded')
    
    
#  if commandReceiver:
#     commandReceiver.join()

if telemetrySender:
     telemetrySender.join()

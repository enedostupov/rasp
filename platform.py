from SerialInitializer import SerialInitializer
from CommandReceiver import CommandReceiver
from TelemetrySender import TelemetrySender
import serial

control_response = '900001#'
control_port = 6001

telemetry_response = '900002#'
telemetry_port = 6002

control_serial = None
commandReceiver = None
telemetry_serial = None
telemetrySender = None

serialInitializer = SerialInitializer('900000#')
print('SerialInitializer - done')

control_serial_device_name = serialInitializer.get_port_by_response(control_response)
print('control_serial_device_name - done')
if control_serial_device_name:
    print('control port was founded')
#    control_serial = serial.Serial(control_serial_device_name, 9600)
#    commandReceiver = CommandReceiver('', control_port, 7, control_serial)
#    commandReceiver.start()
else:
    print('control port was not founded')

telemetry_serial_device_name = serialInitializer.get_port_by_response(telemetry_response)
print('telemetry_serial_device_name - done')
if telemetry_serial_device_name:
    print('telemetry port was founded')
#    telemetry_serial = serial.Serial(telemetry_serial_device_name, 9600)
#    telemetrySender = TelemetrySender('', telemetry_port, 7, telemetry_serial)
#    telemetrySender.start()
else:
    print('telemetry port was not founded')

# if commandReceiver:
#     commandReceiver.join()

# if telemetrySender:
#     telemetrySender.join()

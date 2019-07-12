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

control_serial_device_name = serialInitializer.get_port_by_response(control_response)
if control_serial_device_name:
    control_serial = serial.Serial(control_serial_device_name, 9600)
    commandReceiver = CommandReceiver('', control_port, 7, control_serial)
    commandReceiver.start()

telemetry_serial_device_name = serialInitializer.get_port_by_response(telemetry_response)
if telemetry_serial_device_name:
    telemetry_serial = serial.Serial(control_serial_device_name, 9600)
    telemetrySender = TelemetrySender( '', telemetry_port, 7, telemetry_serial)
    telemetrySender.start()

if commandReceiver:
    commandReceiver.join()

if telemetrySender:
    telemetrySender.join()

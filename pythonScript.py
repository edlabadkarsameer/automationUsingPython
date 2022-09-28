import serial
import time

ser = serial.Serial('COM4', 9600)  # open serial port
time.sleep(2)                      # wait 2 seconds
ser.name()
'COM4'
ser.write(b'H')
# LED turns on
ser.write(b'L')
# LED turns off

ser.write(b'H')
# LED turns on

ser.write(b'L')
# LED turns off
#SameerEdlabadkar
ser.close()
exit()

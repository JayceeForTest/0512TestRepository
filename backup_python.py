import serial
from pyfirmata import Arduino,SERVO,util
from time import sleep

# Communicate with Arduino
arduino = serial.Serial('COM3',9600)
sleep(2)
def move_Servo(servo,angle):
    arduino.write(255)
    arduino.write(servo)
    arduino.write(angle)
    move_Servo(9,45)
    
    # Using pyfirmata
    port = 'COM3'
    pin = 9
    angle = 45
    board = Arduino(port)
    sleep(2)
    board.digital[pin].mode = SERVO
    def rotateServo(pin,angle):
        board.digital[pin].write(angle)
        sleep(0.015)
    while True:
        for i in range(0,90):
            rotateServo(pin,i)
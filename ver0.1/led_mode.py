import RPi.GPIO as GPIO
import socket
import time

R,G,B=18,15,14

GPIO.setmode(GPIO.BCM)

GPIO.setup(R, GPIO.OUT)
GPIO.setup(G, GPIO.OUT)
GPIO.setup(B, GPIO.OUT)

pwmR = GPIO.PWM(R, 70)
pwmG = GPIO.PWM(G, 70)
pwmB = GPIO.PWM(B, 70)

pwmR.start(0)
pwmG.start(0)
pwmB.start(0)

HOST = '192.168.0.8'
PORT = 11010

while True:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.8',11010))
    #s.sendall('b8-27-eb-9f-15-29')
    s.sendall('0')
    data = s.recv(1024)
    if(data == 'close'):
        pwmR.ChangeDutyCycle(0)
        pwmG.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
    else:
        R_L = data[0:3]
        G_L = data[3:6]
        B_L = data[6:9]
        pwmR.ChangeDutyCycle(int(R_L))
        pwmG.ChangeDutyCycle(int(G_L))
        pwmB.ChangeDutyCycle(int(B_L))
    print 'success'
    s.close()
    time.sleep(1)

pwmR.stop()
pwmG.stop()
pwmB.stop()

GPIO.cleanup()
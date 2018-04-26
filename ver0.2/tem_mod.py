import RPi.GPIO as GPIO
import time
import socket

HOST = '192.168.163.129'
PORT = 11010

channel = 9
data = []
j = 0

GPIO.setmode(GPIO.BCM)

time.sleep(1)

GPIO.setup(channel, GPIO.OUT)

GPIO.output(channel, GPIO.LOW)
time.sleep(0.02)
GPIO.output(channel, GPIO.HIGH)

GPIO.setup(channel, GPIO.IN)

while GPIO.input(channel) == GPIO.LOW:
    continue

while GPIO.input(channel) == GPIO.HIGH:
    continue

while j < 40:
    k = 0
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        k += 1
        if k > 100:
            break
    if k < 8:
        data.append(0)
    else:
        data.append(1)

    j += 1

print 'sensor is working'
print data

hum_bit = data[0:8]
hum_po_bit = data[8:16]
tem_bit = data[16:24]
tem_po_bit = data[24:32]
check_bit = data[32:40]

hum = 0
hum_po = 0
tem = 0
tem_po = 0
check = 0

for i in range(8):
    hum += hum_bit[i] * 2 ** (7-i)
    hum_po += hum_po_bit[i] * 2 ** (7-i)
    tem += tem_bit[i] * 2 ** (7-i)
    tem_po += tem_po_bit[i] * 2 ** (7-i)
    check += check_bit[i] * 2 ** (7-i)

tmp = hum + hum_po + tem + tem_po

if check == tmp:
    print 'temperature is :' , tem , '\nhumidity is :', hum
    while True:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        data = s.recv(1024)
        if(data == 'need'):
            s.sendall(str(tmp))
        time.sleep(1)
    s.close()
else:
    print 'error'
    print 'temperature :', tem ,'\nhumidity :', hum ,'\ncheck :', check ,'\ntmp :', tmp

GPIO.cleanup()
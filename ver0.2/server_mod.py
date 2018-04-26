from SocketServer import BaseRequestHandler,ThreadingTCPServer
import threading
import transfer

global device
device = ['192.168.0.8']
global light
light = '000000000'
class Handler(BaseRequestHandler):
    def handle(self):
        global device
        global light
        address,pid = self.client_address
        if address not in device:
            device.append(address)
        print 'connected', address,device
        while True:
            data = self.request.recv(1024)
            if data == 'led':
                self.request.sendall(transfer.LData())
                print 'done'
            else:
                self.request.sendall('need')
                print 'tem or bright'
                transfer.TData(data)
                break

if __name__ == '__main__':
    HOST = '192.168.163.129'
    PORT = 11010
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler)
    print 'listing'
    server.serve_forever()
print server

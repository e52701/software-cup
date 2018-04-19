from SocketServer import BaseRequestHandler,ThreadingTCPServer
import threading

class Handler(BaseRequestHandler):
    def handle(self):
        x = 0
        light = ['100000000','000100000','000000100']
        address,pid = self.client_address
        print 'connected', address
        while True:
            data = self.request.recv(1024)
            if len(data) > 0:
                print 'receive ', data
                cur_thread = threading.current_thread()
                if x < 2:
                    self.request.sendall(light[x])
                    x += 1
                else:
                    self.request.sendall('000000000')
                    x = 0
            else:
                print 'close'
                break

if __name__ == '__main__':
    HOST = '192.168.163.129'
    PORT = 11010
    ADDR = (HOST,PORT)
    server = ThreadingTCPServer(ADDR,Handler)
    print 'listing'
    server.serve_forever()
print server

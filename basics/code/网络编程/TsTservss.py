# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 创建一个SocketSercerTCP服务器
"""

from SocketServer import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handel(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(),
                                      self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
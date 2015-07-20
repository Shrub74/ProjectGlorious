#-------------------------------------------------------------------------------
# Client for ProjectGlorious
# 10/7/15
#-------------------------------------------------------------------------------

import socket

s = socket.socket()
host = socket.gethostname()
port = 40404

s.connect((host, port))
print s.recv(1024)
s.close()

#-------------------------------------------------------------------------------
# Server for ProjectGlorious connection
# Shrub
# 10/7/15
#-------------------------------------------------------------------------------

import socket

s = socket.socket()
host = socket.gethostname()
port = 40404
s.bind((host, port))

s.listen(5)
while True: 
    c, addr = s.accept()
    print "Connection received from", addr
    c.send("Thank you for connecting")
    c.close()

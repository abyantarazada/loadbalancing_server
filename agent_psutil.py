import os
import socket
import psutil
import pickle
import time

def server_usage():
    usage = (psutil.virtual_memory().percent + psutil.cpu_percent())/2
    return pickle.dumps(usage)
    
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
while True:
    server.connect(('192.168.56.101', 5000))
    server.send(server_usage())
    time.sleep(1)

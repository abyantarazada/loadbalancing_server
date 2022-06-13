import os
import socket
import psutil
import pickle
import time

def memory_usage():
    memory = psutil.virtual_memory().percent
    return pickle.dumps(memory)

def cpu_usage():
    cpu = psutil.cpu_percent()
    return pickle.dumps(cpu)

def server_usage():
    usage = (memory_usage() + cpu_usage())/2
    return pickle.dumps(usage)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
while True:
    server.connect(('192.168.56.101', 5000))
    server.send(server_usage())
    time.sleep(1)

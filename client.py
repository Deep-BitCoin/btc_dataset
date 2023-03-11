#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Authbor: Deep BitCoin Team.
# Date: 2023-03-01
# Version: 1.0
# Where: Tokyo, Japan

import socket
import sys

class CLIENT():
    def __init__(self,host,port,savefile="./data.bin"):
        self.c = socket.socket()
        self.host = host
        self.port = port
        self.c.connect((self.host,self.port))
        self.savefile = savefile

    def run(self):


        argv = " ".join(sys.argv)
        self.c.send(argv.encode('utf-8'))
        while True:
            recv_data = self.c.recv(1024)
            if recv_data:
                recv_data = recv_data.decode("utf-8")

                if  '###DOWNLOAD###' == recv_data :
                    print(" === Download ===")
                    file_size = self.c.recv(1024)
                    file_size = int(file_size.decode("utf-8"))
                    f = open(self.savefile, 'wb')
                    received_size = 0

                    while received_size < file_size:
                        size = 0  
                        if file_size - received_size > 1024:  
                            size = 1024
                        else:  
                            size = file_size - received_size
                        data = self.c.recv(size)  
                        data_len = len(data)
                        received_size += data_len
                        print('received：', int(received_size / file_size * 100), "%")
                        f.write(data)

                else:
                    print(recv_data)

            else:
                self.c.close()
                break


def main():

    s = CLIENT("154.221.28.77",9999,savefile="./data.bin")
    s.run()

if __name__ == "__main__":
    main()

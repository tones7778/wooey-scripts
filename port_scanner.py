#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import argparse
import sys
from datetime import datetime


parser = argparse.ArgumentParser(description="Port scan a host from a starting port to end port.")
parser.add_argument('host', help="Please enter a host to scan.", type=str, default="kvm01.home.lan")
parser.add_argument('start_port', help="Pleas enter a starting port.", type=int, default=2000)
parser.add_argument('end_port', help="Pleas enter a end port.", type=int, default=2100)

def main():
    args = parser.parse_args()

    t1 = datetime.now()
    ports_found = []

    try:
        for port in range(int(args.start_port), int(args.end_port)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            print("Checking port: {}".format(port))
            result = sock.connect_ex((args.host, port))
            #print(result)
            if result == 0:
                ports_found.append(port)
                print("Port: {} Open".format(port))
            sock.close()
    except KeyboardInterrupt:
        sys.exit()


    t2 = datetime.now()
    print("Scanning completed in: {}".format(t2-t1))
    print("Found ports: {}".format(ports_found))

if __name__ == '__main__':
    sys.exit(main())

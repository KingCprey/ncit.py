#!/usr/bin/env python3
#This will function the same as TCP file transfer when using netcat with a few extra features
import os,socket,ipaddress,argparse

def _command_nc_receive(receive_port):
    return "nc "

def parse_args(args=None,interactive=True):
    parser=argparse.ArgumentParser()
    parser.add_argument("-g","--generate",action="store_true",help="Generate the command to send/recv with netcat")
    parser.add_argument("-s","--send",action="store_true",help="Send a file")
    parser.add_argument("-r","--recv",action="store_true",help="Receive a file")
    parser.add_argument("-l","--listen",action="store_true",help="Start up a file receiving server")
    parser.add_argument("-p","--port",type=int,help="The port to listen on or remote port (depending on action)",action="store")
    parser.add_argument("-P","--local-port",type=int,help="The local port to use (overrides -p on recv)",action="store")
    parser.add_argument("-v","--verbose",nargs="?",default=1,help="Set the verbosity level")
    if not interactive:parser.add_argument("-I","--interactive",action="store_true",help="Start the program in interactive mode")
    return parser.parse_args(args)
def main():
    a=parse_args()

if __name__=="__main__":
    main()

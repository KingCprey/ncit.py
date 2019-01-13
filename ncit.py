#!/usr/bin/env python3
#This will function the same as TCP file transfer when using netcat with a few extra features
import os,socket,ipaddress,argparse
import getpass,shutil
def inp(prompt=">",password_protect=False):
    if password_protect:return getpass.getpass(prompt)
    else:
        try:return raw_input(prompt)
        except:return input(prompt)
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
    parser.add_argument("files",nargs="+",help="The list of files to send/location to store incoming file")
    return parser.parse_args(args)

def send_file(file_path,recv_host,recv_port,local_host=None,local_port=None,retry=True,retry_count=5):
    if not os.path.exists(file_path):raise FileNotFoundError(file_path)
    if os.path.isdir(file_path):
        #compress dir into a single file to send over network.
        raise NotImplementedError("Directory archiving not implemented yet lmao")
    elif not os.path.isfile(file_path):
        raise FileNotFoundError("idk what to do with this lmao")
    if local_host is None:local_host=""
    if local_port is None:local_port=0
    conn=None
    retries=0
    while retries<retry_count and retry:
        try:
            conn=socket.create_connection((recv_host,rect_port),source_address=(local_host,local_port))
            break
        except:
            print("Failed to connect to %s:%s"%(recv_host,recv_port))
            retries+=1
    with open(file_path,'rb')as inp:
        print("Starting file transfer")
        #In future, implement own copying so can present transfer progress
        shutil.copyfileobj(inp,conn)
        print("File sent")

def main():
    a=parse_args()
    port=a.port
    if not port is None:
        #0 only allowed on receiveing, on sending will also throw an error
        if port<0 or port > 65535:
            raise ValueError("Invalid port supplied, must be 0-65535")
    if a.generate:
        raise NotImplementedError()
    elif a.send:
        if port is None:
            #raise ValueError("No receiving port specified, use -p")
            recv_port_raw=inp("Receiving port: ")
            try:
                recv_port=int(recv_port_raw)
                if recv_port<=0 or port>65535:print("Port must be between 0-65536")
                else:port=recv_port
            except:print("Failed to parse '%s' as integer"%recv_port_raw)
        #ayy we managed to get a successful port
        if port is not None:
            pass
    elif a.listen:
        pass
    elif a.recv:
        pass


if __name__=="__main__":
    main()

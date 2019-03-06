#!/usr/bin/env python3
#This will function the same as TCP file transfer when using netcat with a few extra features
import os,socket,ipaddress,argparse
import getpass,shutil
import datetime
import transport
from utils import *
#5 second default timeout
DEFAULT_TIMEOUT=5

def parse_args(args=None,interactive=True):
    parser=argparse.ArgumentParser()
    parser.add_argument("-g","--generate",action="store_true",help="Generate the command to send/recv with netcat")
    parser.add_argument("-s","--send",action="store_true",help="Send a file")
    parser.add_argument("-r","--recv",action="store_true",help="Receive a file")
    #parser.add_argument("-R","--recv-text",action="store_true",help="Show the command needed to receive the file")
    parser.add_argument("-t","--timeout",type=float,help="Specify the timeout (in seconds) when establishing TCP connection")
    parser.add_argument("-R","--retries",type=int,help="Specify the amount of retries to attempt when establishing TCP connection")
    parser.add_argument("-l","--listen",action="store_true",help="Start up a file receiving server")
    parser.add_argument("-p","--port",type=int,help="The port to listen on or remote port (depending on action)",action="store")
    parser.add_argument("-P","--local-port",type=int,help="The local port to use (overrides -p on recv)",action="store")
    parser.add_argument("-v","--verbose",nargs="?",default=1,help="Set the verbosity level")
    parser.add_argument("-c","--compress",action="store_true",help="Use with sending to send multiple files in single transmission (in an archive) (default: false)")
    parser.add_argument("-A","--archive-type",action="store",help="Specify the type of archive to send the file as")
    parser.add_argument("--list-archives",action="store_true",help="List the file types able to archive files into")
    if not interactive:parser.add_argument("-I","--interactive",action="store_true",help="Start the program in interactive mode")
    parser.add_argument("files",nargs="+",help="The list of files to send/location to store incoming file")
    return parser.parse_args(args)

def _prep_files(file_list):
    if len(file_list)>0:
        if len(file_list)>1:
            pass
    else:raise ValueError("No files supplied lmao")
def main():
    a=parse_args()
    print(a)
    if a.list_archives:
        exit()
    port=a.port
    if not port is None:
        #0 only allowed on receiveing, on sending will also throw an error
        if port<0 or port > 65535:
            exit(_logtext(Log.LOG_ERROR,"Invalid port supplied, must be 0-65535"),exit_code=1)
    def _require_port(prompt="Endpoint port: "):
        if port is None:
            recv_port_raw=inp(prompt)
            try:
                recv_port=int(recv_port_raw)
                if recv_port<=0 or port>65535:exit(_logtext(LOG_ERROR,"Port must be between 0-65536"),exit_code=1)
                else:port=recv_port
            except:
                exit(_logtext(Log.LOG_ERROR,"Failed to parse '%s' as integer"%recv_port_raw),exit_code=1)
    if a.generate:
        raise NotImplementedError()
    elif a.send:
        flen=len(a.files)
        if flen>0:
            if flen>1 or not os.path.isfile(a.files[0]):
                raise NotImplementedError()
                #log(Log.LOG_INFO,"Combining ")
            elif os.path.isfile():
                transport.send_file()
        else:
            exit(_logtext(Log.LOG_ERROR,"No files supplied"))
        if port is None:
            _require_port()
        #ayy we managed to get a successful port
        if port is not None:
            pass

    elif a.listen:
        pass
    elif a.recv:
        pass

if __name__=="__main__":
    main()

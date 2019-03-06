import socket,os,tarfile
from utils import *

def send_file(file_path,recv_host,recv_port,local_host=None,local_port=None,retry=True,retry_count=5,timeout=5):
    if not os.path.exists(file_path):raise FileNotFoundError(file_path)
    if not os.path.isfile(file_path):
        raise ValueError("\"%s\" is not a file"%file_path)
    """
    if os.path.isdir(file_path):
        #compress dir into a single file to send over network.
        raise NotImplementedError("Directory archiving not implemented yet lmao")
    elif not os.path.isfile(file_path):raise FileNotFoundError("idk what to do with this lmao")
    """
    if not local_host:local_host=""
    if not local_port:local_port=0
    conn=None
    retries=0
    file_size=os.path.getsize(file_path)
    while retries<retry_count and retry:
        try:
            conn=socket.create_connection((recv_host,rect_port),timeout=timeout,source_address=(local_host,local_port))
            log(Log.LOG_INFO,"Successfully connected to %s:%s")
            break
        except:
            log(Log.LOG_ERROR,"Failed to connect to %s:%s.%s"(recv_host,recv_port,"Attempt %s of %s"%(retries+1,retry_count)))
            retries+=1
    with open(file_path,'rb')as inp:
        log(Log.LOG_INFO,"Starting file transfer")
        #In future, implement own copying so can present transfer progress
        for complete,amount_written in copyfileobj(inp,conn):
            percentage=int((amount_written/file_size)*100.0)
            log(Log.LOG_INFO," [Transfer] %s of %s bytes (\%%s complete)"%(amount_written,file_size,percentage))
        log(Log.LOG_INFO,"Transfer Complete")

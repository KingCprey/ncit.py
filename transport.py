import socket,os,tarfile
from utils import *
def establish_connection(recv_host,recv_port,local_host=None,local_port=0,retry=True,retry_count=3,timeout=5,silent=False):
    retries=0
    while True:
        try:
            if not silent:log(Log.LOG_CONNECTION,"Attempting TCP connection to {0}:{1}",recv_host,recv_port)
            conn=socket.create_connection((recv_host,recv_port),timeout=timeout,source_address=(local_host,local_port))
            if not silent:log(Log.LOG_CONNECTION,"Successfully connected to {0}:{1}",recv_host,recv_port)
            return conn
        except socket.timeout:
            if not silent:log(Log.LOG_ERROR,"Connection timed out to {0}:{1}.{2}",)
        except Exception as e:
            if not silent:log(Log.LOG_ERROR,"Connection failed. Unknown error occured")
            raise e
        if retries>=retry_count or not retry:break

def send_file(file_path,connection):
    if not os.path.exists(file_path):raise FileNotFoundError(file_path)
    if not os.path.isfile(file_path):
        raise ValueError("\"%s\" is not a file"%file_path)
    """
    if os.path.isdir(file_path):
        #compress dir into a single file to send over network.
        raise NotImplementedError("Directory archiving not implemented yet lmao")
    elif not os.path.isfile(file_path):raise FileNotFoundError("idk what to do with this lmao")
    """
    file_size=os.path.getsize(file_path)
    with open(file_path,'rb')as inp:
        log(Log.LOG_INFO,"Starting file transfer")
        #In future, implement own copying so can present transfer progress
        for complete,amount_written in copyfileobj(inp,conn):
            percentage=int((amount_written/file_size)*100.0)
            log(Log.LOG_INFO," [Transfer] %s of %s bytes (\%%s complete)"%(amount_written,file_size,percentage))
        log(Log.LOG_INFO,"Transfer Complete")

import tarfile,zipfile,ipaddress
try:
    import bz2
    BZIP2_SUPPORTED=True
except:BZIP2_SUPPORTED=False
try:
    import lzma
    LZMA_SUPPORTED=True
except:LZMA_SUPPORTED=False
def inp(prompt=">",password_protect=False):
    if password_protect:return getpass.getpass(prompt)
    else:
        try:return raw_input(prompt)
        except:return input(prompt)
class Log:
    LOG_CONNECTION="SOCKET"
    LOG_INFO="INFO"
    LOG_ERROR="ERROR"
DEFALUT_COPY_BUFFER=64*1024 #64KB
def copyfileobj(src,dest,length=0,do_yield=True):
    if not length:length=DEFAULT_COPY_BUFFER
    amount_written=0
    while True:
        buf=src.read(length)
        if not buf:break
        dest.write(buf)
        amount_written+=len(buf)
        #yield returns (complete,amount_written)
        if do_yield:yield False,amount_written
    if do_yield:yield True,amount_written
    else:return amount_written

def get_time(format="%H:%M:%S"):return datetime.datetime.now().strftime(format)
#literally just print but puts the time first
def _logtext(logtype,msg,*args):return "%s%s: %s"%(get_time(),"" if logtype is None or len(logtype.strip())==0 else " %s"%logtype,msg.format(*args))
def log(logtype,msg,*args):print(_logtext(logtype,msg,*args))
def exit(msg=None,exit_code=0):
    if msg:print(msg)
    elif type(msg)==int:exit_code=msg
    sys.exit(exit_code)
def exiterr(exit_code,logtype,msg,*args):exit(_logtext(logtype,msg,*args),exit_code)
def _bzip2_supported():return BZIP2_SUPPORTED
def _lzma_supported():return LZMA_SUPPORTED
def validate_int(s):
    try:
        int(s)
        return True
    except:return False
#allow_listening means that 0 is allowed as a port
def validate_port(s,listening=False):
    if validate_int(s):
        p=int(s)
        return (p>=0 if listening else p>0) and p<=65535
    return False
def validate_ip(addr):
    try:
        ipaddress.ip_address(addr)
        return True
    except ValueError:return False
def _get_addresses(hostname):
    addrinfo=socket.getaddrinfo(hostname,None)
    addresses=[]
    for tup in addrinfo:
        ad=tup[5][0]
        if not ad in addresses:addresses.append(ad)
    return addresses
def validate_hostname(hostname,return_addr=False):
    try:
        addr=_get_addresses(hostname)
        return True,addr if return_addr else True
    except:return False,None if return_addr else False

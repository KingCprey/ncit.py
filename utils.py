import tarfile,zipfile
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
    LOG_INFO="INFO"
    LOG_ERROR="ERROR"
DEFALUT_COPY_BUFFER=64*1024 #64KB
def copyfileobj(src,dest,length=0,yield=True):
    if not length:length=DEFAULT_COPY_BUFFER
    amount_written=0
    while True:
        buf=src.read(length)
        if not buf:break
        dest.write(buf)
        amount_written+=len(buf)
        #yield returns (complete,amount_written)
        if yield:yield False,amount_written
    if yield:yield True,amount_written
    else:return amount_written

def get_time(format="%H:%M:%S"):return datetime.datetime.now().strftime(format)
#literally just print but puts the time first
def _logtext(logtype,msg,*args):return "%s%s: %s"%(get_time(),"" if logtype is None or len(logtype.strip())==0 else " %s"%logtype,msg.format(*args))
def log(logtype,msg,*args):print(_logtext(logtype,msg,*args))
def exit(msg=None,exit_code=0):
    if msg:print(msg)
    elif type(msg)==int:exit_code=msg
    sys.exit(exit_code)

def _bzip2_supported():return BZIP2_SUPPORTED
def _lzma_supported():return LZMA_SUPPORTED

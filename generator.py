import os
DEFAULT_NC_EXEC="nc"
DEFAULT_PORT=16091
class OutputLocation:
    NCIT_DOWNLOADS=1
    USER_DOWNLOADS=2
    HOME=3
    CWD=4
DEFAULT_OUTPUT_LOCATION=OutputLocation.NCIT_DOWNLOADS
def _output_location(location=DEFAULT_OUTPUT_LOCATION):
    if type(location) is int:
        if location==OutputLocation.NCIT_DOWNLOADS:return os.path.join("$HOME",".ncit","downloads")
        elif location==OutputLocation.USER_DOWNLOADS:return os.path.join("$HOME","Downloads")
        elif location==OutputLocation.HOME:return "$HOME"
        elif location=OutputLocation.CWD:return "./"
        else:raise ValueError("Invalid Output Location")
    else:return location
def _mkdir_output_location(location=DEFAULT_OUTPUT_LOCATION):
    return 'mkdir -p \"%s\"' % _output_location(location)

def _nc_receive_tcp(nc_exec=DEFAULT_NC_EXEC,port=DEFAULT_PORT,output_location=None):
    if output_location is None:
        pass
    return "%s -l -p %s > %s" % (nc_exec,port,output_location)

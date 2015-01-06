from socket import socket   
from OpenSSL.SSL import Connection, Context, SSLv3_METHOD
import httplib

def ssl_check(ipaddr):
    try:
        conn = httplib.HTTPSConnection(ipaddr)
        conn.request('HEAD', "/")
        res = conn.getresponse()
        if res.status < 400:
            return True
        return False
    except :
        return False

if __name__ == '__main__':
    server = '208.117.252.45'
    print ssl_check(server)

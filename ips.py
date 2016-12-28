import urllib.request
from lxml import etree
import socks
import socket
import urllib.request

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1080)
socket.socket = socks.socksocket
def ips():      
    url='http://cn-proxy.com/'
    html=urllib.request.urlopen(url).read()
    tree=etree.HTML(html)
    ips=tree.xpath('//table[1]/tbody/tr/td[1]/text()')
    ports=tree.xpath('//table[1]/tbody/tr/td[2]/text()')
    f=[]#新建列表，用以保存代理信息
    for i in range(len(ips)):
        f.append(ips[i]+':'+ports[i])#将代理ip端口追加到列表中
    return f

import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.amazon.com.br/?tag=desktopbr-20')
except urllib.error.URLError:
    print('site não esta acessivel no momento')
else:
    print ('site acessivel no momento')
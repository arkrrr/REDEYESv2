
import socket
class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
def cek_ip():
  hostname = socket.gethostname()
  IPAddr = get('https://api.ipify.org').text
  print (bcolors.HIJAU,"Nama host kamu adalah :" + hostname)
  print (bcolors.KUNING,"iP Address perangkat kamu adalh:" + IPAddr)
  print (bcolors.ENDC," ")

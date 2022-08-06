import  socket

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def port_scanner():
  socket.setdefaulttimeout(1)
  scan=(input("masukkan ip address target:"))
  daftar_port=[20,21,22,23,25,53,79,80,110,137,138,139,443,445,3306] # bisa di tambahkan portnya
  try:
      print (bcolors.UNGU,"#####################################")
      for port in daftar_port:
          socket_obj = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          result=socket_obj.connect_ex((scan,int(port)))
          if result==0:
              print (bcolors.HIJAU,"[+]Terbuka port : " + str(port))
              socket_obj.close()
          else:
              print(bcolors.MERAH,"[!]Tertutup port : " + str(port))
              socket_obj.close()
              print (bcolors.ENDC," ")
  except KeyboardInterrupt:
      print('stop')



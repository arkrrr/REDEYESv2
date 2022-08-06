import hashlib

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def membuat_md5():
  plaintext = input("nilai string :")
  md5 = hashlib.md5()
  md5.update(plaintext.encode("ascii"))
  print (bcolors.UNGU,"nilai hash md5:",md5.hexdigest())
  print (bcolors.ENDC," ")


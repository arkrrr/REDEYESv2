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

def membuat_sha1():
  plaintext = input("Nilai string :")
  sha = hashlib.sha1()
  sha.update(plaintext.encode("ascii"))
  print (bcolors.HIJAU,"nilai hash sha1 adalah:",sha.hexdigest())
  print (bcolors.ENDC," ")

import hashlib
import time

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def md5_cracking():
  counter = 1
  md5_hash = input("Hash md5 : ")
  pwdfile = input("alamat worldlist : ")
  
  try:
    pwdfile = open(pwdfile,"r")
  except:
    print (bcolors.MERAH,"\nFile tidak di temukan")
    quit()
  
  try:
    for password in pwdfile:
        md5 = hashlib.md5()
        md5.update(password.strip().encode('ascii'))
        start = time.time()
        print (bcolors.HIJAU,"[*]Coba password %d: %s " % (counter,password.strip()))
        time.sleep(0.1)
    
        counter += 1
        end = time.time()
        t_time = end - start
    
        if md5_hash.strip() == md5.hexdigest():
            print (bcolors.HIJAU,"\n[+]Password ditemukan.\nPassowrdnya adalah : %s" % password.strip())
            print  ("Total waktu : ", t_time,"second")
            time.sleep(10)
            break
        else:
            print (bcolors.MERAH,"\n[!]Password tidak di temukan")
            print (bcolors.ENDC," ")
  except KeyboardInterrupt:
      print ('stop') 

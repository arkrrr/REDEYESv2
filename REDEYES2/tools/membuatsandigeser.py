class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def sandi_geser():
  z=['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N',  'O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m',  'n','o','p','q','r','s','t','u','v','w','x','y','z']
  print("Sandi Geser")
  a = input("\Masukkan kata = ")
  b = ""
  geser = 7
  for x in range(len(a)):
          temp = z.index(a[x]) + geser
          b=b+z[temp%63]
  print(bcolors.UNGU,"\nPlainText = "+a)
  print(bcolors.KUNING,"CipherText = "+b)
  print (bcolors.ENDC," ")

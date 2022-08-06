import zipfile

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



file = input("Masukkan direktori file (../../file.zip) : ")
wordlist = input("Masukkan wordlist (wordlist.txt): ")
try:
    a = zipfile.ZipFile(file)
except FileNotFoundError:
    print (bcolors.UNGU,'File target tidak di temukan')
try:
    pwdfile = open(wordlist, 'r')
except FileNotFoundError:
    print (bcolors.MERAH,'File wordlist tidak di temukan')

c = 0


try:
    for d in pwdfile.readlines():
        password = d.strip()
        try:
            c += 1
            a.extractall(pwd=password)
            print (bcolors.HIJAU,"[+]Password di temukan : {password}")
            break
        except:
            c += 1
            print (bcolors.MERAH,f"[-] Gagal : {password}")
except:
    exit()

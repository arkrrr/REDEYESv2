import os , requests

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def admin_finder():
    wordlist = input("Masukkan alamat wordlist (wordlist.txt): ")

    try:
        wordlist = open(wordlist,'r')
    except:
        print(bcolors.MERAH,"file tidak di temukan")

    try:
        kontent = wordlist.read()
        x = kontent.split('\n')
    except AttributeError:
        exit()

    target = input("Masukkan target: ")

    for i in x:
        url=target+"/"+i
        code=requests.get(str(url)).status_code
        if code == 200:
                 print (bcolors.HIJAU, "[+]Berhasil | url : "+url)
        else:
                 print (bcolors.MERAH, "[-] Gagal | url:" + url)


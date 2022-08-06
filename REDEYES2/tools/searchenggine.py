from googlesearch import search

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def search_enggine():
    query = input("Masukkan keywords: ")
    try:
        for j in search(query, tld='com', num=10, stop=100):
            print (bcolors.HIJAU,j,"\n")
    except KeyboardInterrupt:
        print ("stop")


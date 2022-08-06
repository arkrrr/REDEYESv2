class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_email():
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  def check(email):
    if(re.search(regex,email)):
        print(bcolors.HIJAU,"Valid email")
    else:
        print(bcolors.MERAH,"Invalid email")
        print (bcolors.ENDC," ")
  if __name__ == '__main__':
    email = input("Enter email address:")
    check(email)

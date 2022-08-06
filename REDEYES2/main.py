import tools

class bcolors:
    UNGU = '\033[95m'
    BIRU = '\033[94m'
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def banner():
  print (bcolors.MERAH,"""

.::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"

""")

  print (bcolors.MERAH,"""
 _______  _______  ______   _______           _______  _______ 
(  ____ )(  ____ \(  __  \ (  ____ \|\     /|(  ____ \(  ____ \
| (    )|| (    \/| (  \  )| (    \/( \   / )| (    \/| (    \/
| (____)|| (__    | |   ) || (__     \ (_) / | (__    | (_____ 
|     __)|  __)   | |   | ||  __)     \   /  |  __)   (_____  )
| (\ (   | (      | |   ) || (         ) (   | (            ) |
| ) \ \__| (____/\| (__/  )| (____/\   | |   | (____/\/\____) |
|/   \__/(_______/(______/ (_______/   \_/   (_______/\_______)v2
                                                               

          """)

  print (50*"=")
  print ("\n")
  print (bcolors.BIRU,"                Red Eyes versi 2.0")
  print ("\n")
  print (bcolors.MERAH,50*"-")
  print (bcolors.UNGU," # Di buat oleh arkrrr")
  print (bcolors.HIJAU," #Yang merasa kurang sama script ini tenang aja nanti akan di update^_^")
  print (bcolors.KUNING,"hubungi saya di: arkrrr755@gmail.com")
  print (bcolors.ENDC," ")

banner()

def show_menu():
    print (bcolors.BOLD,bcolors.MERAH,"[1] port scanner")
    print (bcolors.BOLD,bcolors.MERAH,"[2] membuat md5 ")
    print (bcolors.BOLD,bcolors.MERAH,"[3] membuat sha1")    
    print (bcolors.BOLD,bcolors.MERAH,"[4] membuat sandi geser")
    print (bcolors.BOLD,bcolors.MERAH,"[5] check email")
    print (bcolors.BOLD,bcolors.MERAH,"[6] md5 cracking")
    print (bcolors.BOLD,bcolors.MERAH,"[7] brute email")
    print (bcolors.BOLD,bcolors.MERAH,"[8] brute force web direktori")
    print (bcolors.BOLD,bcolors.MERAH,"[9] search enggine")
    print ("\n")
    menu = input("pilih no > ")
    
    if menu == '1':
        bcolors.KUNING,tools.port_scanner()
    elif menu == '2':
        tools.membuat_md5()
    elif menu == '3':
        tools.membuat_sha1()
    elif menu == '4':
        tools.sandi_geser()
    elif menu == '5':
        tools.check_email()
    elif menu == '6':
        tools.md5_cracking()
    elif menu == '7':
        tools.bruteEmail()
    elif menu == '8':
        tools.admin_finder()
    elif menu == '9':
        tools.search_enggine()
    else:
        print ("pilihan tidak valid")


show_menu()
jawab = 'y'
while (True):
    jawab = input("ulang lagi tidak (y/n) ? ")
    if jawab == 'y':
        show_menu()
        print ("\n")
    elif jawab =='n':
        exit()

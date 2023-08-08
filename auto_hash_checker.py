import time
import hashlib
import os
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

# Verificar as hash's de varios ficheiros


#og hash's


og_hash_t1 = "174423d7a70fed8464cbf7bfb38a610acc561ff0990996a6329b633f58b3fa7c"
og_hash_t2 = "dd320dcf69a46527e7ea43bd91591e07006d59123aab82524389555cf097c761"
og_hash_t3 = "688787d8ff144c502c7f5cffaafe2cc588d86079f9de88304c26b0cb99ce91c6"



#caminhos
target1 = 'C:\\Users\\nunoc\\meus docs'
target2 = 'C:\\Users\\nunoc\\meus docs\\varios dbs\\varios\\varios volume.txt'
target3 = 'C:\\Users\\nunoc\\meus docs\\ghfj.txt'


def get_hash(tg):
    h = hashlib.new("SHA256")


    with open(tg,'rb') as file:
        chunk = 0
        while chunk!=b'':
            chunk = file.read(1024)
            h.update(chunk)

        return h.hexdigest()


    #Transformar a target em bytes
    #b = bytes(tg, 'UTF-8')


   # h.update(b)

    #print(h.digest())
    #return h.hexdigest()


gh = get_hash(target3)

if(og_hash_t3 == gh):
    print(f"Target: {target3}",Fore.GREEN + "\nOriginal hash:",og_hash_t3, Fore.GREEN + "\nCurrent hash: ",gh, Fore.GREEN + "\n Match!")
else:
    print(f"Target: {target3}", Fore.GREEN + "\nOriginal hash:", og_hash_t3, Fore.RED + "\nCurrent hash: ", gh, Fore.RED + "\n Different Hash!")
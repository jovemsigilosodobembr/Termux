import os, time 

PURPLE="\033[1;35m"
RED='\033[1;31m'
NC='\033[0m'

def banner():
    print('''\033[33m
    
=====================================    
 _                                 
| |                                
| |_ ___ _ __ _ __ ___  _   ___  __ CYAN="\033[1;36m"
| __/ _ \ '__| '_ ` _ \| | | \ \/ /
| ||  __/ |  | | | | | | |_| |>  < 
 \__\___|_|  |_| |_| |_|\__,_/_/\_\YELLOW="\033[1;33m"
                                   
=====================================

          ===============
          = Gilmar Filho =
        =================
Espero ter te ajudado com esse script\033[m''')
banner()
print('\n')
menu = 0
while menu != 7:
    menu = int(input(('''
    [ 1 ] Termux debian
    [ 2 ] Proprio termux
    [ 3 ] vazio
    [ 4 ] vazio 
    [ 5 ] vazio
    [ 6 ] vazio
    [ 7 ] Sair 
    
    Coloque a opção desejada: ''')))
    
    if menu == 1:    
     os.system('apt update||apt upgrade')

    print('\n')
    
     if menu == 2:
   print("Autualizando os repostitorio")
    os.system("apt update")
    os.system("apt upgrade")
    

    os.system('apt install git')
    os.system("apt get install")
   
    
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3")
    
    print('\n')
    
  
  
    
    elif menu == 7:
     print('Byee')
     time.sleep(2)
     os.system('cls||clear')
    
    

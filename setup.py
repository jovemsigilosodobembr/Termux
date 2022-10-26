import os



CYAN="\033[1;36m"
YELLOW="\033[1;33m"
PURPLE="\033[1;35m"
GREEN="\033[1;32m"
RED='\033[1;31m'
NC='\033[0m'

def banner():
    print('''\033[33m
    
=====================================    
 _                                 
| |                                
| |_ ___ _ __ _ __ ___  _   ___  __
| __/ _ \ '__| '_ ` _ \| | | \ \/ /
| ||  __/ |  | | | | | | |_| |>  < 
 \__\___|_|  |_| |_| |_|\__,_/_/\_\
                                   
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
   print("Autualizando os repostitorio")
    os.system("apt update")
    os.system("apt upgrade")
    
    print("Instalando as dependicias")
    
    os.system('apt install git')
    os.system("apt get install")
    
    print("Instalando o python")
    
    os.system("apt-get install python")
    os.system("apt-get install python2")
    os.system("apt-get install python3")
    
    print("Instalado com sucesso")
    
    print('\n')
    
  
  
    
    elif menu == 7:
     print('Byee')
     time.sleep(2)
     os.system('cls||clear')
    
    

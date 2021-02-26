import os
banner = """                                                                                     
     ______  _______          ____         _____           _____             ______  
    |      \/       \    ____|\   \    ___|\    \     ____|\    \        ___|\     \ 
   /          /\     \  /    /\    \  /    /\    \   /     /\    \      |    |\     \
  /     /\   / /\     ||    |  |    ||    |  |    | /     /  \    \     |    |/____/|
 /     /\ \_/ / /    /||    |__|    ||    |  |____||     |    |    | ___|    \|   | |
|     |  \|_|/ /    / ||    .--.    ||    |   ____ |     |    |    ||    \    \___|/ 
|     |       |    |  ||    |  |    ||    |  |    ||\     \  /    /||    |\     \    
|\____\       |____|  /|____|  |____||\ ___\/    /|| \_____\/____/ ||\ ___\|_____|   
| |    |      |    | / |    |  |    || |   /____/ | \ |    ||    | /| |    |     |   
 \|____|      |____|/  |____|  |____| \|___|    | /  \|____||____|/  \|____|_____|   
    \(          )/       \(      )/     \( |____|/      \(    )/        \(    )/     
     '          '         '      '       '   )/          '    '          '    '      
                                             '                                       """
print(banner)
print("1. install vagrant")
print("2. install virtualbox")
choice = input("$ ")
print(choice)
if choice == "1":
  os.system("curl https://releases.hashicorp.com/vagrant/2.2.14/ --output vagrant_2.2.14_x86_64.msi")
  os.system("vagrant_2.2.14_x86_64.msi")
elif choice == "2":
  os.system("curl https://download.virtualbox.org/virtualbox/6.1.18/ --output VirtualBox-6.1.18-142142-Win.exe")
  os.system("VirtualBox-6.1.18-142142-Win.exe")

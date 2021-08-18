import socket,threading,os
from sys import platform

os.system('cp -r info /tools')

os.chdir("tools")

def linux():
    def main():
        os.system("clear")
        print("OPC 0.4.5 | Coded by \033[0;31mKrisIsHere & \033[0;31mOwenwastaken\033[00m")
        print("What would you like to do?: \n1) Join 2) Host 3) Update 00) Extra: ")
        loopy = True
        while loopy == True:
            xd = input(">")
            if xd == "1":
                os.system("python3 client.py")
            elif xd == "2":
                    os.system("clear")
                    print("Server is up and running!")
                    os.system("python3 server.py")
            elif xd == "3":
                os.chdir('..')
                path = os.getcwd()
                parent = os.path.abspath(os.path.join(path, os.pardir))
                os.system("cp -r tools/.info " + parent)
                os.system("cp -r tools/OPC_update.py " + parent)
                os.system("python3 " + parent + "/OPC_update.py")
                os.chdir('tools')
            elif xd == "00":
                print("about) About help) Help credit) Credits  clear) Clear")
            elif xd == "help":
                os.system("cat info/help.txt")
            elif xd == "about":
                os.system("cat info/about.txt")
            elif xd == "credit":
                os.system("cat info/credit.txt")
            elif xd == "clear":
                main()
    if os.path.isfile(".info/first_time.py"):
        main()
    else:
        loooop = True
        while loooop == True:
            tos_1 = input("Would you like to to read the first time launch manual(\033[0;33mY/\033[0;33mN\033[00m): ")
            if tos_1 in ["Y", "y"]:
                print("If you wanna connect to a server you need to know whoever is running that server will have access to your IP address.\nIf you wanna host a server you need to know that whoever connects to it will have your IP address. To run a server you need to open port 14900 on your network.")
                loooop = False
                lmao = input("Do you wish to continue? (\033[0;33mY/\033[0;33mN\033[00m): ")
                if lmao in ["y", "Y"]:
                    os.system("mkdir .info ; touch .info/first_time.py")
                    os.system("clear")
                    main()

            else:
                xd = input("Are you sure you dont wanna read it? (\033[0;33mY/\033[0;33mN\033[00m): ")
                if xd in ["y", "Y"]:
                    os.system("mkdir .info ; touch .info/first_time.py")
                    loooop = False
                    main()

if platform == "linux" or platform == "linux2":
    os.system('clear')
    linux()
elif platform == "win32":
    print("sorry bruv windows support been dropped")
else:
    print("Platform not supported")
    exit()

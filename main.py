import socket,threading,os
from sys import platform

if platform == "win32":
    os.system('copy info tools')
else:
    os.system('cp -r info /tools')

os.chdir("tools")

def win():
    input("Warning: Windows is not completely supported in the main branch of OPC. It is recomended that you use the owen-dev branch for better compatibility. Press ENTER to continue")
    os.system('cls')
    def main():
        os.system('cls')
        print("OPC 0.4.2 | Coded by \033[0;31mKrisIsHere\033[97;40m & \033[0;31mOwenwastaken\033[97;40m")
        print("What would you like to do?: \n\033[92;40m1\033[97;40m) Join \033[92;40m2\033[97;40m) Host \033[92;40m3\033[97;40m) Update \033[92;40m00\033[97;40m) Extra: ")
        loopy = True
        while loopy == True:
            xd = input(">")
            if xd == "1":
                loopy = False
                os.system("client.py")
            elif xd == "2":
                    os.system("cls")
                    print("Server is up and running!")
                    os.system("python server.py")
            elif xd == "3":
                """
                os.chdir('..')
                path = os.getcwd()
                parent = os.path.abspath(os.path.join(path, os.pardir))
                os.system("copy tools/.info tools" + parent)
                os.system("copy -r tools/OPC_update.py " + parent)
                os.system("python " + parent + "/OPC_update.py")
                os.chdir('tools')
                """
                print("The online updater currently does not work with windows.")
                print("This issue will be fixed soon.")
            elif xd == "00":
                print("\033[92;40mabout\033[97;40m) About \033[92;40mhelp\033[97;40m) Help \033[92;40mcredit\033[97;40m) Credits  \033[92;40mclear\033[97;40m) Clear")
            elif xd == "help":
                os.system("type info/help.txt")
            elif xd == "about":
                os.system("type info/about.txt")
            elif xd == "credit":
                os.system("type info/credit.txt")
            elif xd == "clear":
                main()
    if os.path.isfile(".info/first_time.py"):
        main()
    else:
        loooop = True
        while loooop == True:
            tos_1 = input("Would you like to to read the first time launch manual(\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
            if tos_1 == "y":
                print("xd")
                os.system("mkdir .info ; touch .info/first_time.py")
                loooop = False
                main()
            elif tos_1 == "Y":
                print("If you wanna connect to a server you need to know whoever is running that server will have access to your IP address.\nIf you wanna host a server you need to know that whoever connects to it will have your IP address. To run a server you need to open port 14900 on your network.")
                loooop = False
                lmao = input("Do you wish to continue? (\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
            if lmao == "y":
                os.system("mkdir .info ; touch .info/first_time.py")
                os.system("cls")
                main()
            if lmao == "Y":
                os.system("mkdir .info ; touch .info/first_time.py")
                os.system("cls")
                main()

            else:
                xd = input("Are you sure you dont wanna read it? (\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
                if xd == "y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    loooop = False
                    main()
                if xd == "Y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    loooop = False
                    main()


def linux():
    os.chdir("..")
    os.system("cp -r info tools")
    os.chdir("tools")
    def main():
        os.system("clear")
        print("OPC 0.4.2 | Coded by \033[0;31mKrisIsHere\033[97;40m & \033[0;31mOwenwastaken\033[97;40m")
        print("What would you like to do?: \n\033[92;40m1\033[97;40m) Join \033[92;40m2\033[97;40m) Host \033[92;40m3\033[97;40m) Update \033[92;40m00\033[97;40m) Extra: ")
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
                print("\033[92;40mabout\033[97;40m) About \033[92;40mhelp\033[97;40m) Help \033[92;40mcredit\033[97;40m) Credits  \033[92;40mclear\033[97;40m) Clear")
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
            tos_1 = input("Would you like to to read the first time launch manual(\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
            if tos_1 == "y":
                print("xd")
                os.system("mkdir .info ; touch .info/first_time.py")
                loooop = False
                main()
            elif tos_1 == "Y":
                print("If you wanna connect to a server you need to know whoever is running that server will have access to your IP address.\nIf you wanna host a server you need to know that whoever connects to it will have your IP address. To run a server you need to open port 14900 on your network.")
                loooop = False
                lmao = input("Do you wish to continue? (\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
                if lmao == "y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    os.system("clear")
                    main()
                if lmao == "Y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    os.system("clear")
                    main()

            else:
                xd = input("Are you sure you dont wanna read it? (\033[0;33mY\033[97;40m/\033[0;33mN\033[92;40m\033[97;40m): ")
                if xd == "y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    loooop = False
                    main()
                if xd == "Y":
                    os.system("mkdir .info ; touch .info/first_time.py")
                    loooop = False
                    main()

if platform == "linux" or platform == "linux2":
    os.system('clear')
    linux()
elif platform == "win32":
    os.system('cls')
    win()
else:
    print("Platform not supported")
    sys.exit()

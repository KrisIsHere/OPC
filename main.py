import socket,threading,os
from sys import platform
import CompatibilityModules as CM

CM.copy("info", "tools")
os.chdir("tools")

def win():
        def chat():
                nickname = input("Choose your \033[0;31mnickname\033[97;40m: ")
                server = input("Enter \033[92;40mserver \033[0;31mIP\033[97;40m: ")

                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((server, 14900))

                def receive():
                    while True:
                        try:
                            message = client.recv(1024).decode('ascii')
                            if message == 'NICK':
                                client.send(nickname.encode('ascii'))
                            else:
                                print(message)
                        except:
                            print("An error occured!")
                            client.close()
                            break

                def write():
                    while True:
                        message = '\033[0;31m{}\033[97;40m:\033[92;40m {}\033[97;40m'.format(nickname, input(''))
                        client.send(message.encode('ascii'))

                receive_thread = threading.Thread(target=receive)
                receive_thread.start()

                write_thread = threading.Thread(target=write)
                write_thread.start()

        def main():
            CM.clearscreen()
            print("OPC 0.4 | Coded by \033[0;31mKrisIsHere\033[97;40m & \033[0;31mOwenwastaken\033[97;40m")
            print("What would you like to do?: \n\033[92;40m1\033[97;40m) Join \033[92;40m2\033[97;40m) Host \033[92;40m3\033[97;40m) Update \033[92;40m00\033[97;40m) Extra: ")
            loopy = True
            while loopy == True:
                xd = input(">")
                if xd == "1":
                    chat()
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


def linux():
        def chat():
        nickname = input("Choose your \033[0;31mnickname\033[97;40m: ")
        server = input("Enter \033[92;40mserver \033[0;31mIP\033[97;40m: ")

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, 14900))

        def receive():
            while True:
                try:
                    message = client.recv(1024).decode('ascii')
                    if message == 'NICK':
                        client.send(nickname.encode('ascii'))
                    else:
                        print(message)
                except:
                    print("An error occured!")
                    client.close()
                    break

        def write():
            while True:
                message = '\033[0;31m{}\033[97;40m:\033[92;40m {}\033[97;40m'.format(nickname, input(''))
                client.send(message.encode('ascii'))

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()

            def write():
                while True:
                    message = '\033[0;31m{}\033[97;40m:\033[92;40m {}\033[97;40m'.format(nickname, input(''))
                    client.send(message.encode('ascii'))

            receive_thread = threading.Thread(target=receive)
            receive_thread.start()

            write_thread = threading.Thread(target=write)
            write_thread.start()

    def main():
        os.system("clear")
        print("OPC 0.4 | Coded by \033[0;31mKrisIsHere\033[97;40m & \033[0;31mOwenwastaken\033[97;40m")
        print("What would you like to do?: \n\033[92;40m1\033[97;40m) Join \033[92;40m2\033[97;40m) Host \033[92;40m3\033[97;40m) Update \033[92;40m00\033[97;40m) Extra: ")
        loopy = True
        while loopy == True:
            xd = input(">")
            if xd == "1":
                chat()
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

CM.clearscreen()
if platform == "linux" or platform == "linux2":
    linux()
elif platform == "win32":
    win()
else:
    print("Platform not supported")
    sys.exit()

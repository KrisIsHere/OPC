import os
import sys
from sys import platform
path = os.getcwd()
parent = os.path.abspath(os.path.join(path, os.pardir))
os.chdir(parent)
print(os.getcwd())
print("OPC update tool made by KrisIsHere | ver. 0.3")
xd = input("Would you like to update? (Y/N): ")
if xd == "Y":
    os.system("rm -rf OPC ; git clone https://github.com/krisishere/OPC ; cp -r .info " + parent + "/OPC/tools/")
    os.system("rm -rf .info")
    os.chdir(parent + "/OPC")
    os.system("python3 main.py")
    sys.exit()
if xd == "y":
    os.system("rm -rf OPC ; git clone https://github.com/krisishere/OPC ; cp -r .info " + parent + "/OPC/tools/")
    os.system("rm -rf .info")
    os.chdir(parent + "/OPC")
    os.system("python3 main.py")
    sys.exit()
else:
    print("ok")
    sys.exit()

import requests
import sys
import re

from colorama import Fore, init
init()


def checkURL():
    with open(sys.argv[1], "r") as f:
        url = f.read()
        links = re.findall(r'https?://[^\s<>"].[^\s<>"]+', url)

    for link in links:
        print(link)
        r = requests.get(link)
        if str(r) == "<Response [200]>":
            print(Fore.GREEN + str(r) + " Response Good!" + Fore.RESET)
        elif str(r) == "<Response [400]>" or str(r) == "<Response [404]>":
            print(Fore.RED + str(r) + " Response Bad! There may be a problem with the website." + Fore.RESET)
        else:
            print(str(r) + " Response Unknown!")


if len(sys.argv) > 1:
    if sys.argv[1] != "v" and sys.argv[1] != "version":
        checkURL()
    else:
        print("deadlinkz v0.1")
        print("Made by IcemanEtika")
else:
    print('\033[91m' + "No arguments inputted. The correct usage is main.py insert_website_here.html" + '\033[0m')
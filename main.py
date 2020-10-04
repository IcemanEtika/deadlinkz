import argparse
import requests
import threading
import sys
import re

from colorama import Fore, init
init()

def checkGood(links):
    for link in links:
        try:
            r = requests.head(link, timeout=10)  # gets the status code of the website
            if 200 <= r.status_code <= 299:
                print(Fore.GREEN + str(link) + " " + str(r) + " Good!" + Fore.RESET)
        except:
            continue


def checkBad(links):
    for link in links:
        try:
            r = requests.head(link, timeout=10)  # gets the status code of the website
            if 200 < r.status_code > 299:
                if 200 < r.status_code > 299 and 400 <= r.status_code <= 599:
                    print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage." + Fore.RESET)
        except requests.exceptions.RequestException:
            print(Fore.RED + "Error: could not connect to website " + str(link) + "!")
        except requests.exceptions.Timeout:
            print(Fore.RED + "Error: connection to website " + str(link) + " timed out!")
        finally:
            continue


def checkURL():
    try:
        with open(sys.argv[2], "r") as f:
            links = re.findall(r'https?://[^\s<>"].[^\s<>"]+', f.read())  # find all urls and add them to the links array

        if sys.argv[1] == "-g" or sys.argv[1] == "--good":
            checkGood(links)
        elif sys.argv[1] == "-b" or sys.argv[1] == "--bad":
            checkBad(links)
        else:
            for link in links:
                try:
                    r = requests.head(link, timeout=10)  # gets the status code of the website
                    if 200 <= r.status_code <= 299:
                        print(Fore.GREEN + str(link) + " " + str(r) + " Good!" + Fore.RESET)
                    elif 400 <= r.status_code <= 599:
                        print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage." + Fore.RESET)
                    else:
                        print(str(link) + " " + str(r) + " Unknown!")
                except requests.exceptions.RequestException:
                    print(Fore.RED + "Error: could not connect to website!")
                except requests.exceptions.Timeout:
                    print(Fore.RED + "Error: connection to website timed out!")
                finally:
                    continue
    except FileNotFoundError:
        print(Fore.RED + "Error: the file could not be opened.")


# Create parser that allows for arguments to be used with the tool (-a, --all, -v, --version, -h, --help)
parser = argparse.ArgumentParser(description='Checks for dead urls in a file')
parser.add_argument('-a', '--all', help='Checks urls in text file (e.g, main.py -c index.html)')
parser.add_argument('-g', '--good', help='Displays all good links in file')
parser.add_argument('-b', '--bad', help='Displays all bad links in file')
parser.add_argument('-v', '--version', action="version", version='deadlinkz v0.1', help='Displays version info')
args = parser.parse_args()

threading.Thread(target=checkURL()).start()

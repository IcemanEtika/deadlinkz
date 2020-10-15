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

def checkWithoutIgnoredLink(links):
    try:
        # Check the ignored text file from argument[3]
        with open(sys.argv[3], "r") as i:
            texts = i.read().splitlines();

        if isValidTextFile(texts):
            # collect URL from text file
            r = re.compile('https?://[^\s<>"].[^\s<>"]+')
            ignoredLinks = list(filter(r.match, texts))
            ignored = False

            for link in links:
                try:
                    if len(ignoredLinks) > 0:
                        for ig in ignoredLinks:
                            if re.match(ig, link):
                                ignored = True
                                break
                        if ignored:
                            ignored = False
                            continue
                        else:
                            ignored = False
                            r = requests.head(link, timeout=10)  # gets the status code of the website
                            if 200 <= r.status_code <= 299:
                                print(Fore.GREEN + str(link) + " " + str(r) + " Good!" + Fore.RESET)
                            elif 400 <= r.status_code <= 599:
                                print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage." + Fore.RESET)
                                exitCode.append(1);
                            else:
                                print(str(link) + " " + str(r) + " Unknown!")
                        
                        
                    else:
                        r = requests.head(link, timeout=10)  # gets the status code of the website
                        if 200 <= r.status_code <= 299:
                            print(Fore.GREEN + str(link) + " " + str(r) + " Good!" + Fore.RESET)
                        elif 400 <= r.status_code <= 599:
                            print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage." + Fore.RESET)
                            exitCode.append(1);
                        else:
                            print(str(link) + " " + str(r) + " Unknown!")
                except requests.exceptions.RequestException:
                    print(Fore.RED + "Error: could not connect to website!")
                except requests.exceptions.Timeout:
                    print(Fore.RED + "Error: connection to website timed out!")
                finally:
                    exitCode = 1;
                    continue
            
        else:
            raise NotImplementedError
    except NotImplementedError:
        exitCode = 2;
        print(Fore.RED + "Error: Invalid text file")   

# Check the available text file that include all of condition for lab4 and return boolean 
def isValidTextFile(links):
    if len(links) == 0: # Check empty file, If file is empty, Check every URLs
        result = True
    for link in links:
        if link[0] == "#": # '#' is comment line
            result = True
        elif re.match(r'https?://[^\s<>"].[^\s<>"]+', link): # Check URL that include (http://, https://)
            result = True
        else: # if not, Go to ignore text file error
            return False
    return result

def checkURL():
    exitCode = 0;
    try:
        with open(sys.argv[2], "r") as f:
            links = re.findall(r'https?://[^\s<>"].[^\s<>"]+', f.read())  # find all urls and add them to the links array

        if sys.argv[1] == "-g" or sys.argv[1] == "--good":
            checkGood(links)
        elif sys.argv[1] == "-b" or sys.argv[1] == "--bad":
            checkBad(links)
        elif sys.argv[1] == "-i" or sys.argv[1] == "--ignore": 
            checkWithoutIgnoredLink(links)
        else:
            for link in links:
                try:
                    r = requests.head(link, timeout=10)  # gets the status code of the website
                    if 200 <= r.status_code <= 299:
                        print(Fore.GREEN + str(link) + " " + str(r) + " Good!" + Fore.RESET)
                    elif 400 <= r.status_code <= 599:
                        print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage." + Fore.RESET)
                        exitCode.append(1);
                    else:
                        print(str(link) + " " + str(r) + " Unknown!")
                except requests.exceptions.RequestException:
                    print(Fore.RED + "Error: could not connect to website!")
                except requests.exceptions.Timeout:
                    print(Fore.RED + "Error: connection to website timed out!")
                finally:
                    exitCode = 1;
                    continue
    except FileNotFoundError:
        exitCode = 2;
        print(Fore.RED + "Error: the file could not be opened.")

    sys.exit(exitCode)

# Create parser that allows for arguments to be used with the tool (-a, --all, -v, --version, -h, --help)
parser = argparse.ArgumentParser(description='Checks for dead urls in a file')
parser.add_argument('-a', '--all', help='Checks urls in text file (e.g, main.py -c index.html)')
parser.add_argument('-g', '--good', help='Displays all good links in file')
parser.add_argument('-b', '--bad', help='Displays all bad links in file')
parser.add_argument('-v', '--version', action="version", version='deadlinkz v0.1', help='Displays version info')
parser.add_argument('-i', '--ignore', nargs='+', help='Displays all links witout ignored link in file') # Check URLs without ignored file's url
args = parser.parse_args()

threading.Thread(target=checkURL()).start()
sys.exit(0)

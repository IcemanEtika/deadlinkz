import argparse
import requests
import sys
import re

from colorama import Fore, init
init()


def checkURL():
    try:
        with open(sys.argv[2], "r") as f:
            url = f.read()
            links = re.findall(r'https?://[^\s<>"].[^\s<>"]+', url)  # find all urls and add them to the links array

        for link in links:
            r = requests.get(link)  # gets the status code of the website
            if 200 <= r.status_code <= 299:
                print(Fore.GREEN + str(link) + " " + str(r) + " Good!")
            elif 400 <= r.status_code <= 599:
                print(Fore.RED + str(link) + " " + str(r) + " Bad! There may be a problem with the webpage.")
            else:
                print(str(link) + " " + str(r) + " Unknown!")
    except FileNotFoundError:
        print(Fore.RED + "Error: the file could not be opened.");


# Create parser that allows for arguments to be used with the tool (-c, --check, -v, --version, -h, --help)
parser = argparse.ArgumentParser(description='Checks for dead urls in a file')
parser.add_argument('-c', '--check', help='Checks urls in text file (e.g, main.py -c index.html)')
parser.add_argument('-v', '--version', action="version", version='deadlinkz v0.1', help='Displays version info')
args = parser.parse_args()

checkURL()


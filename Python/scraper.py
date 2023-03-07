from bs4 import BeautifulSoup
from alive_progress import alive_bar
from alive_progress.styles import showtime
import sys
import argparse
import requests
import time


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("-h","--help", action="help", help="Enter an URL and it will be downloaded")
parser.add_argument("url", help="URL to be inserted")
tagcommands = parser.add_argument_group("Elements")
tagcommands.add_argument("-a", "--link",action="store_true", help="Extracts all hyperlinks")
tagcommands.add_argument("-p","--text",action="store_false", help="Extracts all paragraph text")
parser.parse_args()
url = sys.argv[1]
firstarg = sys.argv[2]
if firstarg == "-a" or firstarg == "--link":
    firstarg = "a"
elif firstarg == "-p" or firstarg == "--text":
    firstarg = "p"


if len(sys.argv) < 2:
    raise Exception("Error: Not enough arguments presented")

headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    }
website = requests.get(url=url, headers=headers)
website.raise_for_status()
print("Response Received")

website.encoding = "utf-8"

SoupTest = BeautifulSoup(website.text, "html.parser")
with open('test.html', 'w', encoding='utf-8') as testfile:
    testfile.write(SoupTest.prettify())
with open("info.txt", 'w') as outputfile:
    with open("test.html", "r") as readfile:
        with alive_bar(len(SoupTest.find_all(firstarg)), title="Downloading", bar="notes", spinner="fish") as bar:
            for site in SoupTest.find_all(firstarg):
                if firstarg == "p":
                    bar.text = f'-> getting element {str(site.text)}, please wait'
                    outputfile.write("\t" + (str(site.text) + '\n'))
                elif firstarg == "a":
                    if "http" in str(site.get("href")) or "https" in str(site.get("href")):
                        bar.text = f'-> getting element {str(site.get("href"))}, please wait'
                        outputfile.write((str(site.get("href")) + '\n'))
                time.sleep(0.2)
                bar()
    SoupTest.prettify()
print(url + " was downloaded")

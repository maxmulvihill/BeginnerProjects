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
parser.parse_args()
url = sys.argv[1]
if len(sys.argv) != 2:
    raise Exception("Error: Specified length of arguments is not correct")

headers = {

        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

    }
website = requests.get(url=url, headers=headers)
print("Response Received")


SoupTest = BeautifulSoup(website.text, "html.parser")
with open('test.html', 'w', encoding='utf-8') as testfile:
    testfile.write(SoupTest.prettify())
with open("info.txt", 'w') as outputfile:
    with open("test.html", "r") as readfile:
        with alive_bar(len(SoupTest.find_all('a')), title="Downloading") as bar:
            for site in SoupTest.find_all('a'):
                bar.text = f'-> getting link {str(site.get("href"))}, please wait'
                outputfile.write((str(site.string) + " | " + (str(site.get("href"))) + '\n'))
                time.sleep(0.2)
                bar()
    SoupTest.prettify()
        

print(url + " was downloaded")

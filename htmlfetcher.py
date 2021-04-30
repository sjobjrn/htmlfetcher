import requests
import sys
import time
import click
from requests.exceptions import ConnectionError

@click.command()
@click.option("-o", "--one", "one", help="example htmlfetcher -o https://google.se")
def htmlfetcher(one):
    """[htmlfetcher] - fetch htmls.. pipe a list or use option."""
    if one:
        url = one
        r = requests.get(url)
        shorturl = url.replace('http://','').replace('https://','')
        filename = shorturl + ".html"
        file = open(filename, "w")
        file.write(r.text)

    else:
        for line in sys.stdin:
            try:
                url = line.strip()
                time.sleep(2)
                r = requests.get(url)
                shorturl = url.replace('http://','').replace('https://','')
                filename = shorturl + ".html"
                file = open(filename, "w")
                file.write(r.text)
                print("Fetched {}".format(url))
                print(r.status_code, r.reason)
            except ConnectionError:
                print("{} Failed!".format(url))



if __name__ == '__main__':
    htmlfetcher()


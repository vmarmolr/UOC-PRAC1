import requests
import time 
from bs4 import BeautifulSoup 

##Modificar User Agent
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

## Web a la q accedim
pagina="https://ca.wikipedia.org/wiki/La_guerra_de_les_gal%C3%A0xies"





page=requests.get(pagina, headers=headers)
##print(page.status_code)
soup = BeautifulSoup(page.content, features="html.parser")
print(soup.prettify())

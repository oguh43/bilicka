import os
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "slova.TXT"), encoding="utf8")
ls = f.read().split("\n")
q = str(input("Veta? ")).split(" ")
ls = []
for i in q:
    url = "https://slovnik.aktuality.sk/synonyma/?q="+i
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.findAll("a")
    cry = soup.findAll(class_ = "term")
    halp = "".join(cry[1].stripped_strings)
    halp_moar = halp.split("\"")
    ls.append(halp_moar[-1])
print(" ".join(ls))

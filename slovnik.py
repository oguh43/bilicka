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
#ls = f.read().split(" ")
"""
print(ls)
ls = [i.split(" ") for i in ls]
slovnik = {}

for i in ls:
    #slovnik[i[0]] = i[1]
    print(i)
    print(i[0])
#print(slovnik)

for i in range(len(ls)):
    print(ls[i][0])
    print(ls[i][1])
    slovnik[ls[i][0]] = ls[i][-1]

print(slovnik)

a = str("Moje meno je Hugo").split(" ")
res = []

for i in a:
    if i in slovnik:
        res.append(slovnik[i])
    else:
        res.append(i)
print(" ".join(res))


for i in range(len(ls)):
    print(ls[i][1] , end = " ")
    print(ls[i][0])
"""
"""
url = "https://slovnik.aktuality.sk/synonyma/?q="+input()
#url = "https://slovnik.aktuality.sk/synonyma/?q=ahoj"
#url = "https://slovnik.aktuality.sk/synonyma/?q=abstinent"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup.findAll("a")
print(soup.findAll(class_ = "term"))




cry = soup.findAll(class_ = "term")
print("_______________________")
print(cry[1])
halp = "".join(cry[1].stripped_strings)
print(halp)
halp_moar = halp.split("\"")
print(halp_moar)
"""

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

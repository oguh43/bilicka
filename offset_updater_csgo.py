import urllib.request, json
with urllib.request.urlopen("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json") as url:
    data = json.loads(url.read().decode())
    print(data)
    print(type(data))
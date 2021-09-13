import requests

hesielko = input("hesielko")
email = input("email")
auth = {
    "agent": {
        "name": "Minecraft",
        "version": 1

    },
    "username": email,
    "password": hesielko,
    
}
r = requests.post("https://authserver.mojang.com/authenticate",json=auth)
print(r.text)

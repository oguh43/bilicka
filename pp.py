import os
import json
import requests

import praw

def DownloadImages(subreddit_name: str, amount: int, folder: str = "reddit", ext: list = [".jpg",".png"]) -> None:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if not os.path.exists(__location__ + "\\" + folder):
        os.makedirs(__location__ + "\\" + folder)
    #else:
    #    count = 1
    #    while True:
    #        if not os.path.exists(__location__ + "\\" + folder + "_" + str(count)):
    #            os.makedirs(__location__ + "\\" + folder + "_" + str(count))
    #            folder = folder + "_" + str(count)
    #            break
    #        count += 1
    path = __location__ + "\\" + folder
    print(path)
    url = "https://www.reddit.com/"

    with open(os.path.join(__location__, "credentials.json"), "r") as f:
        data = json.load(f)
        print(data)
    
    reddit = praw.Reddit(
                    client_id=data['client_id'],
                    client_secret=data['api_key'],
                    password=data['password'],
                    user_agent='<reddit_top> accessAPI:v0.0.1 (by/u/imagedownloaderuwu)',
                    username=data['username']
    )

    subreddit = reddit.subreddit(subreddit_name)

    count = 0

    for sub in subreddit.new(limit=amount*2):
        if count == amount:
            break
        else:
            url = (sub.url)
            if not url.endswith(tuple(ext)):
                continue
            count += 1
            r = requests.get(url)
            with open(os.path.join(path,str(count)+".png"), "wb") as f:
                f.write(r.content)

DownloadImages("furry", 50)
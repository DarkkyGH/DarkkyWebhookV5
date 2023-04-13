import threading, requests, os, random
from colored import fg, attr
from itertools import cycle
from pystyle import Write, Colors, Colorate
from time import strftime, gmtime
from datetime import datetime

session = requests.Session()

a = fg('#a005ed')
b = attr('reset')
c = fg('#00D7D3')

web = Write.Input(f"[Darkky] Webook: ", Colors.rainbow, interval=0.0025)

rando = ["Darkky.", "Darkky :)"]

spam = Write.Input(f"[Darkky] Message: ", Colors.rainbow, interval=0.0025)

avatars = cycle([
    "https://media.discordapp.net/attachments/1095425428048584716/1095738881359499366/HD-wallpaper-skull-light-minimal-skull-minimalism-minimalist-dark-black.jpg"
])

proxies = open('proxies.txt').read().split('\n')


def ehook(webhook):

    now = datetime.now()
    s = now.strftime("%S")
    x = f'{strftime(f"[%H:%M:{s}]", gmtime())} Sent Webhook {spam}'
    yes = f'{strftime(f"[%H:%M:{s}]", gmtime())}'
    proxy = cycle(proxies)

    einfo = {
        'username': random.choice(rando),
        'content': spam,
        "avatar_url": next(avatars)
    }
    r = session.post(webhook,
                     json=einfo,
                     proxies={"http": 'http://' + next(proxy)})
    if "retry_after" in r.text:
        print(
            f"{a}{yes}{b} ratelimited sleeping for {a}{r.json()['retry_after']}{b} secs."
        )
    elif r.status_code == 204:
        print(Colorate.Horizontal(Colors.rainbow, x))
    else:
        pass


if __name__ == "__main__":
    os.system('cls & title Darkky Webhook Spammer - Darkky.#2859')
    logo = """
Darkky
      """
    print(Colorate.Horizontal(Colors.rainbow, logo, 3))
    while True:
        for i in range(10):
            threading.Thread(target=ehook, args=(web, )).start()

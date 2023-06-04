#Created by Md. Abedur  Rahman 
#Open_Source
#Cradit Me Bro!

import os
import json
import datetime
import time , requests , random , string
import urllib
#from pyfiglet import Figlet
from rainbowtext import text
from colorama import Fore
def rand_number():
    return str(random.randint(1,999))

def rand_string(number):
    text = string.ascii_letters + string.digits
    result= ''.join(random.choice(text) for ch in range(number))
    return result


session = requests.Session()
url = "https://api.cloudflareclient.com/v0a%s/reg" % rand_number()



def warp_unlimited(id_code):
    inst = rand_string(22)
    body = {"key": "{}=".format(rand_string(43)),
        "install_id": inst,
        "fcm_token": "{}:APA91b{}".format(inst, rand_string(134)),
        "referrer": id_code,
        "warp_enabled": False,
        "locale": "es_US"}
    data = json.dumps(body).encode('utf8')
    header = {'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'okhttp/3.12.1'
        }
    try:
        req = urllib.request.Request(url , data , header)
        resp = urllib.request.urlopen(req)
    except urllib.error.HTTPError:
        time.sleep(5)

        
banner = (f"""     

  /$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$ 
 /$$__  $$| $$__  $$|_  $$_/| $$__  $$
| $$  \ $$| $$  \ $$  | $$  | $$  \ $$
| $$$$$$$$| $$$$$$$   | $$  | $$$$$$$/
| $$__  $$| $$__  $$  | $$  | $$__  $$
| $$  | $$| $$  \ $$  | $$  | $$  \ $$
| $$  | $$| $$$$$$$/ /$$$$$$| $$  | $$
|__/  |__/|_______/ |______/|__/  |__/                                                                     
                                      
\033[41m \033[1;37m           [ABIR RAHMAN]               \x1b[0m
\033[1;32m┌───────────────────────────────────────┐   
\033[1;33m│ [✓] Admin   : MD. ABEDUR RAHMAN\033[1;32m       │
\033[1;34m│ [✓] Github  :\033[41m\033[1;37mD4rK-B0y\x1b[0m                 │
\033[1;35m│ [✓] Whtsapp : 01863517***             │
\033[1;36m│ [✓] Youtube : \x1b[1;32mABID ALL HUB\x1b[1;97m            │               
\033[1;32m└───────────────────────────────────────┘   
\033[1;94m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══
\033[1;97m Status : \033[38;5;46mFREE
\033[1;94m═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━═━══  """)

print (banner)
os.system('xdg-open https://github.com/D4rk-B0y')
print (Fore.RED + "[●] GO 1.1.1.1. VPN AND CLICK 3 LINES AND CLICK ADVANCED OPTION AND CLICK DIAGONSTIC SCROLL AND COPY YOUR WORP ID ")
print (Fore.GREEN + "[●] PASTE YOUR ID AND CLICK ENTER")
print (Fore.LIGHTMAGENTA_EX + "[&] Warp Plus Unlimited Script and Use 1.1.1.1. vpn FREE ! ")
print (Fore.YELLOW + "=====================================") ; code_id = input(Fore.CYAN + "[+] Please Enter Your Client ID : ")
os.system('xdg-open https://github.com/D4rk-B0y')


while True:
    try:
        warp_unlimited(code_id)

        print ( Fore.GREEN + "Success ! You Got 1GB Warp + \n" + Fore.MAGENTA + "Please Wait 10 Second !")
        
        time.sleep(17)
    except KeyboardInterrupt:
        print (Fore.Red + "Stopped ! ")

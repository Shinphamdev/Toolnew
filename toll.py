#Coded by Traodoisub.com
import os,sys
from time import sleep
from datetime import datetime
try:
    import requests
except:
    os.system("pip3 install requests")
    import requests

os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

dem_tong = 0
i_stt=0
listIdTiktok = []
headers = {
    'authority': 'traodoisub.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
    'user-agent': 'traodoisub tiktok tool',
}
def loginTDS (tk, mk):
    try:
        url = "https://traodoisub.com/scr/login.php"
        data = {
            "username": tk,
            "password": mk
        }
        r = requests.post(url, data=data)
        if "success" in r.text:
            return r.cookies
        else:
            return False
    except:
        return False
def login_tds(token):
    try:
        r = requests.get("https://traodoisub.com/api/?fields=profile&access_token="+token, headers=headers).json()
        if 'success' in r:
            os.system("clear")
            print(f" \033[1;32mĐăng nhập thành công!\n User: \033[1;33m{r['data']['user']}\033[1;32m | Xu hiện tại: \033[1;33m{r['data']['xu']}")
            return 'success'
        else:
            print(f" \033[1;31mToken TDS không hợp lệ, hãy kiểm tra lại!\n")
            return 'error_token'
    except:
        return 'error'
def load_job(type_job, token):
    try:
        r = requests.get("https://traodoisub.com/api/?fields="+type_job+"&access_token="+token, headers=headers).json()
        if 'data' in r:
            return r
        elif "countdown" in r:
            sleep(round(r['countdown']))
            print(f" \033[1;31m{r['error']}\n")
            return 'error_countdown'
        else:
            print(f" \033[1;31m{r['error']}\n")
            return 'error_error'
    except:
        return 'error'
def duyet_job(type_job, token, uid):
    try:
        r = requests.get(f'https://traodoisub.com/api/coin/?type={type_job}&id={uid}&access_token={token}', headers=headers).json()
        if "cache" in r:
            return r['cache']
        elif "success" in r:
            dai = f'\033[1;33m------------------------------------------'
            print(dai)
            print(f" \033[1;36mNhận thành công {r['data']['job_success']} nhiệm vụ | \033[1;32m{r['data']['msg']} | \033[1;33m Tổng {r['data']['xu']} Xu")
            print(dai)
            return 'error'
        else:
            print(f"\033[1;31m{r['error']}")
            return 'error'
    except:
        return 'error'
def check_tiktok(id_tiktok, token):
    try:
        r = requests.get("https://traodoisub.com/api/?fields=tiktok_run&id="+id_tiktok+"&access_token="+token, headers=headers).json()
        if 'success' in r:
            os.system("clear")
            print(f" \033[1;32m{r['data']['msg']}|ID: \033[1;33m{r['data']['id']}\033[1;32m")
            return 'success'
        else:
            print(f" \033[1;31m{r['error']}\n")
            return 'error_token'
    except:
        return 'error'

log = loginTDS("cipher1","0962818544sAl@")
if log == False:
    print("Login Thất Bại ")
    sys.exit()
else:
    cookie = log.get("PHPSESSID")
cookies = {
    'PHPSESSID': cookie
}
headers_1 = {
    'authority': 'traodoisub.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://traodoisub.com/view/chtiktok/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',
    'x-requested-with': 'XMLHttpRequest',
}
def get_RQ(url):
    global cookies,headers
    get = requests.get(url, cookies=cookies, headers=headers_1)
    return get



 

token_tds =get_RQ("https://traodoisub.com/view/setting/load.php").json()['tokentds'] 
check_log = login_tds(token_tds)

if check_log == 'success':
    #Nhập user tiktok
    getListtk = get_RQ("https://traodoisub.com/view/chtiktok/").text
    for x in getListtk.split('<tr class="btn-reveal-trigger">'):
        if ('<th class="align-middle text-center white-space-nowrap id">' in x):
            listIdTiktok.append(x.split('target="_blank">')[1].split('</a>')[0])
    while i_stt < int(len(listIdTiktok)):
        # ID tiktok
        print(f" \033[1;33m[{i_stt}] {listIdTiktok[i_stt]}")
        i_stt += 1
    id_tiktok=listIdTiktok[0]
    check_log = check_tiktok(id_tiktok,token_tds)
    ss1=0
    while True :
        #Lựa chọn nhiệm vụ        
        choice = int(1)
        #Nhập delay nhiệm vụ
        delay = int(3)#("\033[1;32m\n Thời gian delay giữa các job (>0 giây):"))
        max_job = int(input("\033[1;32m Dừng lại khi làm được số nhiệm vụ là: "))
        if ss1== 0:
            os.system("clear")
        if choice == 1:
            type_load = 'tiktok_follow'
            type_duyet = 'TIKTOK_FOLLOW_CACHE'
            type_nhan = 'TIKTOK_FOLLOW'
            type_type = 'FOLLOW'
            api_type = 'TIKTOK_FOLLOW_API'
        elif choice == 2:
            type_load = 'tiktok_like'
            type_duyet = 'TIKTOK_LIKE_CACHE'
            type_nhan = 'TIKTOK_LIKE'
            api_type = 'TIKTOK_LIKE_API'
            type_type = 'TYM'
        while True:
            
            list_job = load_job(type_load, token_tds)
            sleep(2)
            if isinstance(list_job, dict) == True:
               for job in list_job['data']:
                    uid = job['id']
                    link = job['link']
                    sleep(1)
                    #os.system(f"termux-open-url {link}")
                    os.system(f"start chrome {LINK}")
                    check_duyet = duyet_job(type_duyet, token_tds, uid)
                    if check_duyet != 'error':
                        dem_tong += 1
                        t_now = datetime.now().strftime("%H:%M:%S")
                        print(f" \033[1;33m[{dem_tong}]\033[1;31m| \033[1;36m{t_now}\033[1;31m|\033[1;35m{type_type}\033[1;31m|\033[1;30m{uid}")
                        if check_duyet > 9:
                            sleep(3)
                            a = duyet_job(type_nhan, token_tds, api_type)
                    if dem_tong == max_job:
                        break
                    else:
                        for i in range(delay,-1,-1):
                            print('\033[1;32m Vui lòng đợi: '+str(i)+' giây',end=("\r"))
                            sleep(1)
            if dem_tong == max_job:
                check_out=input(f"\033[1;32mHoàn thành {max_job} nhiệm vụ!\n \033[1;32m Bạn Muốn Thoát Tool ?(y/n)")
                if check_out =="n" or check_out =="N":
                    dem_tong = 0
                    break
                
                else:
                    sys.exit()

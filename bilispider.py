import requests
import time

request_header = {
    'Accept': 'application/json, text/plain, */*',
'Origin': 'https://www.bilibili.com',
'Referer': 'https://www.bilibili.com/',
'Sec-Fetch-Mode': 'cors',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}

url = 'https://api.bilibili.com/x/web-interface/online'
z = requests.get(url, headers=request_header)
j = z.json()
datas = j['data']

with open('bilidata', 'a') as f:
    f.write(time.asctime(time.localtime()) + ',')
    for i in datas['region_count'].keys():
        f.write(str(datas['region_count'][i]) + ',')
    f.write(str(datas['all_count']) + ',' + str(datas['web_online']) + ',' + str(datas['play_online']) + '\n')
    f.close()
import requests
import json
import time
import pyowm

request_headers = {
'accept': 'application/json, text/javascript, */*; q=0.01',
'referer': 'https://www.ssen.co.uk/ANM/',
'Sec-Fetch-Mode': 'cors',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

# api key using OpenWeatherMap
owm = pyowm.OWM('b3b365b37e36b285df0fc807f8b76c1b')
# get weather conditions in orkney
observation = owm.weather_at_id(2640923)
w = observation.get_weather()

url = "https://www.ssen.co.uk/Sse_Components/Views/Controls/FormControls/Handlers/ActiveNetworkManagementHandler.ashx?action=graph&contentId=14973&_=1571510420656"
z = requests.get(url, headers=request_headers)

jz = z.json()
with open('/root/yf/powerdataset.csv', 'a') as f:
    s = time.asctime(time.localtime()) + ','
    for i in range(5):
        s = s + str(sum(jz['data']['datasets'][i]['data'])) + ','
    s = s + str(w.get_wind()['speed']) + ',' + str(w.get_humidity()) + ',' + str(w.get_temperature('celsius')['temp'])
    s += '\n'
    f.write(s)
    f.close()

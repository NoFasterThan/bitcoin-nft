import requests
# "http://jo123:Pwjustforhack5$@49.254.170.20:8427"
url = 'https://ipinfo.io'
username = 'user-jo1234-sessionduration-1'
password = 'uosai2021'

proxy = f'http://{username}:{password}@us.smartproxy.com:10001'

response = requests.get(url, proxies={'http': proxy, 'https': proxy})

print(response.text)
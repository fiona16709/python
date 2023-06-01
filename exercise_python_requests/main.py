import requests as r

headers = {
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}

response = r.get('https://www.ptt.cc/bbs/Baseball/index.html', headers = headers)

print(response.text)
print(response.status_code)
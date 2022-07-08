import requests
import json

phNo = "8553386541"
country = "in"
url = "https://asia-south1-truecaller-web.cloudfunctions.net/api/noneu/search/v1?q=" + \
    phNo + "&countryCode=" + country

payload = {}
headers = {
  'authority': 'asia-south1-truecaller-web.cloudfunctions.net',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'authorization': 'Bearer a1w05--B05wtx-1VHaZ-8h2aHVUHXPUOz0mIqjRcUCR4A9QQkWgr2bPGJ6KLlbA5',
  'content-type': 'application/json',
  'if-none-match': 'W/"4b3-l6cEKGB7qqdA4yep+D2HeR24RBk"',
  'origin': 'https://www.truecaller.com',
  'referer': 'https://www.truecaller.com/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

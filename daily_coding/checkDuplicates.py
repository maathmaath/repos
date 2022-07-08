import requests
import json

url = "https://stageapp.tekioncloud.xyz/api/documentV2/u/docset/search"


headers = {
  'authority': 'stageapp.tekioncloud.xyz',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'clientid': 'web',
  'content-type': 'application/json',
  'cookie': 'deviceId=280fd527-054c-4441-9669-11196a26b803; redirected_from=https://stageapp.tekioncloud.xyz/core/scanManagement/list/folders; tcookie={%22tekion-api-token%22:%22eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjItMDYtMTRUMDc6MDE6NTIuMjQ1WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjU1MTkwMTEyLCJleHAiOjE2NTUyMjYxMTJ9.ZlTBDBydKl7EqfMf_AHU0Wm0UFJWn-nEgZyHXkq860jznayB6tdP1javH5jgSUtye_VVVRoYaypFB1yNOQf9lbelUJEP_NO2e3_z3W6ruvsQ9sk4YIiTFjdNjR3waswxTYowO8sx6CF4p6AA7YBb7Kqw05ngXBpTZs9RTT-cNaZ-FO0sfKWXnJf8zZ_qIXCJTdtf4-VZ6FORu5q6rsOfPyJ9eenxMr4l2xvCghV9h2QPk-M1B3QlMK9ldvD9qzpnAnzgGz4PMwC14nlHBLvWje5BJvhPx7Y-kcdwWGozaAvAyn3KqO22sIGn8zkxHuzzGWhnSbvWTvxykWy3jHvQPQ%22%2C%22roleId%22:%22113_Controller%22%2C%22userId%22:%2232b87bf1-1361-4c29-953f-871580c4b36d%22%2C%22tenantname%22:%22stg-cacargroup%22%2C%22dealerId%22:%22113%22%2C%22original-userid%22:%2232b87bf1-1361-4c29-953f-871580c4b36d%22%2C%22original-tenantid%22:%22stg-cacargroup%22%2C%22clientId%22:%22web%22%2C%22tek-siteId%22:%22-1_113%22%2C%22locale%22:%22en_US%22}',
  'dealerid': '113',
  'locale': 'en_US',
  'origin': 'https://stageapp.tekioncloud.xyz',
  'original-tenantid': 'stg-cacargroup',
  'original-userid': '32b87bf1-1361-4c29-953f-871580c4b36d',
  'referer': 'https://stageapp.tekioncloud.xyz/core/scanManagement/list/folders',
  'roleid': '113_Controller',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'tek-siteid': '-1_113',
  'tekion-api-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjItMDYtMTRUMDc6MDE6NTIuMjQ1WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjU1MTkwMTEyLCJleHAiOjE2NTUyMjYxMTJ9.ZlTBDBydKl7EqfMf_AHU0Wm0UFJWn-nEgZyHXkq860jznayB6tdP1javH5jgSUtye_VVVRoYaypFB1yNOQf9lbelUJEP_NO2e3_z3W6ruvsQ9sk4YIiTFjdNjR3waswxTYowO8sx6CF4p6AA7YBb7Kqw05ngXBpTZs9RTT-cNaZ-FO0sfKWXnJf8zZ_qIXCJTdtf4-VZ6FORu5q6rsOfPyJ9eenxMr4l2xvCghV9h2QPk-M1B3QlMK9ldvD9qzpnAnzgGz4PMwC14nlHBLvWje5BJvhPx7Y-kcdwWGozaAvAyn3KqO22sIGn8zkxHuzzGWhnSbvWTvxykWy3jHvQPQ',
  'tenantid': 'undefined',
  'tenantname': 'stg-cacargroup',
  'traceparent': '00-4a3dd085aecc3bcf8f73b1e5587a5081-4dd62f98a681d885-01',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'userid': '32b87bf1-1361-4c29-953f-871580c4b36d'
}


def writeFile(data, j):
    fn = f"{j}.json"
    with open(file=fn, mode="w") as f:
        json.dump(data, f)


nextPT = None
dealers = ['113', '4']
for j in dealers:
    payload = json.dumps({
      "sort": [
        {
          "field": "createdTime",
          "order": "DESC"
        },
        {
          "field": "id",
          "order": "ASC"
        }
      ],
      "filters": [],
      "searchText": "",
      "groupBy": [],
      "includeFields": [],
      "searchableFields": [],
      "pageInfo": {
        "start": 0,
        "rows": 9999
      }
    })
    print(f"Running for {j}")
    data1 = []
    headers['dealerid'] = j
    headers['tek-siteid'] = f"-1_{j}"
    for i in range(3):
        print(f"running on rowEnd {(i+1)*9999}")
        response = requests.request(
            "POST", url, headers=headers, data=payload).json()
        if response['data']['nextPageToken']:
            nextPT = response['data']['nextPageToken']
        payload = json.dumps({
          "sort": [
            {
              "field": "createdTime",
              "order": "DESC"
            },
            {
              "field": "id",
              "order": "ASC"
            }
          ],
          "filters": [],
          "searchText": "",
          "groupBy": [],
          "nextPageToken": nextPT,
          "includeFields": [],
          "searchableFields": [],
          "pageInfo": {
            "rows": 9999
          }
        })
        if response['status'] == "success":
            if response['data']['hits']:
                data = response['data']['hits']
                data1.extend(data)
            else:
                break
        else:
            print(f"{j} record failure for {i}")
            print(response)
    writeFile(data1, j)
    print(f"writing data for {j}.txt")

print("task Done")

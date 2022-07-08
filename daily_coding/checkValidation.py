import requests
import json

url = "https://app.tekioncloud.com/api/adminservice/u/userservice/tenant/innovationmotor/dealer/4/user-roles"

payload = json.dumps({
  "sort": [],
  "filters": [
    {
      "field": "active",
      "operator": "IN",
      "values": [
        True
      ],
      "key": "active"
    }
  ],
  "searchText": "",
  "groupBy": [],
  "includeFields": [],
  "searchableFields": [],
  "pageInfo": {
    "start": 0,
    "rows": 50
  }
})
headers = {
  'authority': 'app.tekioncloud.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'clientid': 'web',
  'content-type': 'application/json',
  'cookie': 'fs_uid=rs.fullstory.com#11KA8S#5557932459466752:5905501216808960#9aa6caa9#/1664283303; deviceId=bfa8ec3e-e1d0-4dd1-9df6-d48bf0b7ea3c; redirected_from=https://app.tekioncloud.com/core/user-setup; tcookie={%22tekion-api-token%22:%22eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIyNzlmMzQ5Zi1jNGVlLTQwMjUtYTI0MC1iMTJkNDZjYzk1MGEiLCJpYXQiOjE2NTI4Nzg5MTksInN1YiI6IjI3OWYzNDlmLWM0ZWUtNDAyNS1hMjQwLWIxMmQ0NmNjOTUwYSIsImlzcyI6IkxvZ2luU2VydmljZSIsIm5vdW5jZSI6ImZiY2U5MjY1LWRkZmMtNGUyYS1iY2UxLWJiMzJkYmMyYzI2ZiIsImVtYWlsIjoibWFuanVuYXRoa0B0ZWtpb24uY29tIiwiZXhwIjoxNjUyODg2Njk1fQ.3O-xq9JZpYE071iP58Ctf-cawLqjctKFTIYVvDkgSMA%22%2C%22roleId%22:%224_BDCSuperAdmin%22%2C%22userId%22:%22279f349f-c4ee-4025-a240-b12d46cc950a%22%2C%22tenantname%22:%22techmotors%22%2C%22dealerId%22:%224%22%2C%22original-userid%22:%22279f349f-c4ee-4025-a240-b12d46cc950a%22%2C%22original-tenantid%22:%22techmotors%22%2C%22clientId%22:%22web%22%2C%22tek-siteId%22:%22-1_4%22%2C%22locale%22:%22en_US%22}; _dd_s=logs=1&id=df5e7628-b978-4a23-b7e5-5ecfd8bbcd11&created=1652878595644&expire=1652880247178',
  'dealerid': '4',
  'locale': 'en_US',
  'origin': 'https://app.tekioncloud.com',
  'original-tenantid': 'techmotors',
  'original-userid': '279f349f-c4ee-4025-a240-b12d46cc950a',
  'referer': 'https://app.tekioncloud.com/core/application-settings/user-mimicking',
  'roleid': '4_BDCSuperAdmin',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'tek-siteid': '-1_4',
  'tekion-api-token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNjgiLCJpYXQiOjE2NTI4Nzk0ODAsInN1YiI6IjE2OCIsImlzcyI6IkxvZ2luU2VydmljZSIsIm5vdW5jZSI6IjMzMTg1N2I5LThhNDEtNDljNy05YzNiLTMwYjVjNjFjM2QyOCIsImVtYWlsIjoic3VwZXJhZG1pbkB0ZWNobW90b3JzLmNvbSIsImV4cCI6MTY1Mjg4NzI1Nn0.V8G1An9y6v13VhnRLTqc47EpEQiH_AVy83sV2mQRUZA',
  'tenantid': 'undefined',
  'tenantname': 'techmotors',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
  'userid': '279f349f-c4ee-4025-a240-b12d46cc950a'
}

response = requests.request("POST", url, headers=headers, data=payload)

for i in response.json()['data']['userAndRoleResponses']:
    furl = "https://app.tekioncloud.com/api/adminservice/u/usermimic/tenantId/innovationmotor/userId/" + \
        i['id'] + "/mimicuser/validate"
    payload = json.dumps({})
    response = requests.request("POST", furl, headers=headers, data=payload)
    print(i['displayName'])
    print(response.json()['status'])
    print("\n")

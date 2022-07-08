import json
import requests
a = ['02bbf92d-d379-40b4-9cf6-7356167df595', '0faeb7c9-7401-4b89-9edb-6217217d23c7', '196b7b6a-3cd1-4be9-be8f-a4bcfe3c28c8', '2507b87a-8ff2-44ff-8c7f-20fe0cef27a4', '28bf5b7e-62dd-4c9d-8451-863ed3f5d48d', '2a28fb61-9cc3-47f7-bc1c-05f24863b3cc', '34e73ffc-8882-4fd3-a5c0-3a42a76e015a', '394188b8-4445-4e32-9625-4499e0f2e018', '3d5ffc41-4fef-458c-bd6d-c300369c0077', '3fad06d8-50e0-4163-91ca-0bb65bf8a1c4', '40294581-1472-4807-8b81-55a995ca133a', '433c0cfb-b459-49db-bdfc-3d775d13dda1', '4590c43e-384f-4de9-b26b-4b497ea42710', '57164c6f-99b7-43c3-b66a-da01b86fd219', '589e8555-b49a-44aa-8339-a282ff5b4153', '59442d8a-b1e2-48a2-8aa2-a5804837b504', '60fb6dec-a2b3-4f62-a51b-811aec61f36d', '63fe9e9b-1573-4b50-85a7-f5b8db1a24f3', '69fae23f-b43c-4867-a850-54ae41a92034', '6be016bd-2a91-44ed-a65b-d2be8d998792', '6c85a72d-652d-4f5b-bd2d-a644f65e9d38', '6ef2cf55-fab4-4d81-be0f-b1dbb3a911f6', '6f9d1979-9c9c-407f-8d55-634d2ab0dd98', '736d0743-103f-4b46-b0b8-da09f7cb7f23', '77d3aa12-75e2-4486-8b87-9ab3f15368ec',
     '79673721-4156-408a-bcf3-187b777b1d92', '796eff55-3197-49bd-a1d1-e2f05fc12627', '7a550d37-d24c-4f93-9252-00532ce9bd21', '8a32201e-58a9-4be7-b92f-b8833286045d', '8b62adb6-5e34-4aef-a00f-664d6972029b', '8d11b83a-9cf1-4d7f-838a-a66f5037b87b', '91837152-a5af-4b64-8196-78b723e8f724', '95b19991-ad0d-4489-b3a6-075098112aeb', '9ebd64a6-e2ac-4cf5-b843-ecf6a6d42acb', 'a1586899-f11d-4ee1-981f-4c219b702a63', 'a5b8bcba-7471-477d-86e7-9e58390f7e3c', 'aa35d8f5-8882-4804-b1c4-6f97d99a4338', 'adf12e06-9da2-4ede-aab7-6b42602bda81', 'b0adbe60-137e-444c-ae20-a839aec5a227', 'b0d895a7-e9bd-418f-9c76-dd651b7a89b4', 'b24cb112-b484-472b-a398-2200ba49a945', 'b43d9732-483f-42d5-b7f8-92066b4e3ff8', 'b528789c-ba53-478b-9905-8a883f8d1ebf', 'c1766f21-4dd6-404a-9ab8-bb41ff8f0771', 'c2be0c14-614e-4314-9d71-c4b550b6b180', 'c40558d8-09b8-4a59-b978-a1160d8b54e7', 'c4cdc702-d68d-45a7-bb55-79378a87e67b', 'c55a5d57-84f6-4a55-8af1-f3f449535546', 'c7d35eee-eac6-4433-832d-9af96122f706', 'c839c91e-79dc-43b9-8669-c030ba5786a0']


payload = json.dumps({})
headers = {
  'authority': 'stageapp.tekioncloud.xyz',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'clientid': 'web',
  'content-type': 'application/json',
  'cookie': 'deviceId=55aa9b9d-b45d-4812-8276-9eb3d6d0faf1; amp_8824ef=Eb5-cu0TuM4OHbtEv7lpuM.Z2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20=..1g4d6fret.1g4d7t65i.6.6.c; redirected_from=https://stageapp.tekioncloud.xyz/core/scanManagement/list; tcookie={%22tekion-api-token%22:%22eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjItMDYtMTRUMDU6MjU6MDAuMzc3WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjU1MTg0MzAwLCJleHAiOjE2NTUyMjAzMDB9.AiSfT2h4zHYcd3hqOg1wRc8JN_kb029AKcdG357CS5BdnKu2JVkfcgSK8SbDiUiAVx3wpfXcNypcjxXrFQGYm7oDX4a6gOsu27VnxZaPmY3kpYkIreCaysR1v9Kc6EU7EICROL5gYT418TVycaE6_olV_F7NY1damWDuEtysF9NusBv386EXyorpgE7YmErOpUKTVDm_hfgCeVCs9KEuvIeFPgsDWsnexBOh0jKjaqfmXEUWd8UcrUCDG6fSra2xdumnvmPlr5IYeZs7u_7p_FIkXPgjO1ribJZkDyDdQNwCOfHAreUYbUccjWdOxzEPR7cJ-FSbzNz2-7xHzJY_4Q%22%2C%22roleId%22:%224_SuperAdmin%22%2C%22userId%22:%2232b87bf1-1361-4c29-953f-871580c4b36d%22%2C%22tenantname%22:%22stg-cacargroup%22%2C%22dealerId%22:%224%22%2C%22original-userid%22:%2232b87bf1-1361-4c29-953f-871580c4b36d%22%2C%22original-tenantid%22:%22stg-cacargroup%22%2C%22clientId%22:%22web%22%2C%22tek-siteId%22:%22-1_4%22%2C%22locale%22:%22en_US%22}',
  'dealerid': '4',
  'locale': 'en_US',
  'origin': 'https://stageapp.tekioncloud.xyz',
  'original-tenantid': 'stg-cacargroup',
  'original-userid': '32b87bf1-1361-4c29-953f-871580c4b36d',
  'referer': 'https://stageapp.tekioncloud.xyz/core/application-settings/user-mimicking',
  'roleid': '4_SuperAdmin',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'tek-siteid': '-1_4',
  'tekion-api-token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6SXdOREF3UXpOQk0wRkVNelZFTmpNMU5UQXhSREEzUXpjM1FqVkZNalUxTVRrME1EbERSQSJ9.eyJuaWNrbmFtZSI6ImdhdXJhdnByaW50aW5nIiwibmFtZSI6ImdhdXJhdnByaW50aW5nQG1haWxpbmF0b3IuY29tIiwicGljdHVyZSI6Imh0dHBzOi8vcy5ncmF2YXRhci5jb20vYXZhdGFyLzJiMTZmMzNiYjY1YjNjYzZmOTc1MjI2MDlmMjk0ZDgyP3M9NDgwJnI9cGcmZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGZ2EucG5nIiwidXBkYXRlZF9hdCI6IjIwMjItMDYtMTRUMDU6MjU6MDAuMzc3WiIsImVtYWlsIjoiZ2F1cmF2cHJpbnRpbmdAbWFpbGluYXRvci5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly90ZWtpb24uYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwMzUwMmQ5NmIzYTYzMDA2OGE4OGYyOCIsImF1ZCI6ImxNU3pxYlM3OEVua1hwNXJoWTdaZFZkZHMwQVh2QzRSIiwiaWF0IjoxNjU1MTg0MzAwLCJleHAiOjE2NTUyMjAzMDB9.AiSfT2h4zHYcd3hqOg1wRc8JN_kb029AKcdG357CS5BdnKu2JVkfcgSK8SbDiUiAVx3wpfXcNypcjxXrFQGYm7oDX4a6gOsu27VnxZaPmY3kpYkIreCaysR1v9Kc6EU7EICROL5gYT418TVycaE6_olV_F7NY1damWDuEtysF9NusBv386EXyorpgE7YmErOpUKTVDm_hfgCeVCs9KEuvIeFPgsDWsnexBOh0jKjaqfmXEUWd8UcrUCDG6fSra2xdumnvmPlr5IYeZs7u_7p_FIkXPgjO1ribJZkDyDdQNwCOfHAreUYbUccjWdOxzEPR7cJ-FSbzNz2-7xHzJY_4Q',
  'tenantid': 'undefined',
  'tenantname': 'stg-cacargroup',
  'traceparent': '00-d0c90aa7e038cab2f391f2b721ce73f2-58bded0a887804f4-01',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
  'userid': '32b87bf1-1361-4c29-953f-871580c4b36d'
}

for i in a:
    url = "https://stageapp.tekioncloud.xyz/api/adminservice/u/usermimic/tenantId/mainlineautogroup/userId/" + \
        i + "/mimicuser/validate"
    response = requests.request("POST", url, headers=headers, data=payload)

    print(f"{[i]} {response.json()['status']}")

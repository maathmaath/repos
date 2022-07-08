import json
import requests
from Headers import headers


class Token(object):
    def __init__(self, File=None):
        self.File = File

    def _Text(pList):
        # ord(i)+25+12-13+(13%3)-13-1
        convert_to_text = ''.join(chr(i-25+12-13+(13 % 3)+13+1) for i in pList)
        print(convert_to_text)

    def authorise(self):
        url = self.gClient.open(self.File.get(
            section='access', key='authUrl'))
        response = requests.get(url=url, headers=headers).json()
        if response['status'] == "success":
            return
        self.getAuthorised()

    def getAuthorised(self):
        url = self.gClient.open(self.File.get(
            section='access', key='TokenUrl'))
        username = self.gClient.open(self.File.get(
            section='access', key='username'))
        password = self.gClient.open(self.File.get(
            section='access', key='keyP'))
        password = self._Text(password)
        payload = json.dumps({
            "username": username,
            "password": password
        })
        headers = {
            "Content-Type": "application/json",
            "clientid": "web"
        }
        r = requests.get(url, headers, payload).json()
        mfa_token = r['data']['mfaResponse']['mfaToken']

    def mfaAccess(mfa_token):
        url = "https://preprodapp.tekioncloud.com/api/loginservice/p/authenticate/mfa?dontChallengeMfa=true"
        headers = {
            "Content-Type": "application/json",
            "clientid": "web"
        }
        payload = {
            "tenantId": "techmotors",
            "userId": "b5217a71-5add-4908-bc24-6810be67ed7b",
            "mfaToken": mfa_token,
            "authenticatorType": "GOOGLE_AUTHENTICATOR",
            "otp": "734336"
            }
        r = requests.get(url, headers, payload).json()
        tekion_api_token = r['data']['loginData']['access_token']

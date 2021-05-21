import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
import base64
import requests

baseParams = {}


def sendSingle(unam,pwd,number, message):
    print(number)
    baseParams['username'] = unam
    baseParams['password'] = pwd
    baseParams['to'] = number
    baseParams['content'] = message
    print(baseParams)
    response = urllib.request.urlopen(
        "http://127.0.0.1:1401/send?%s" % urllib.parse.urlencode(baseParams)).read()
    print(response)
    return response


def send_same_message_to_many(uname, pwd, message, numlist):
    print(":Starting")
    url = 'http://127.0.0.1:8080/secure/sendbatch'
    header = {'Authorization': 'Basic a2s6a2s='}
    payload = {
        "messages": [
            {
                "to": [

                ],

            }
        ]
    }
    for num in numlist:
        payload.get("messages")[0].get("to").append(num)
    payload.get("messages")[0].__setitem__("contents", message)
    print(payload)
    response = requests.post(url, headers=header, json=payload)
    print(response.status_code)
    print(response.text)
    return response

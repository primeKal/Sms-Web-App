import urllib.error
import urllib.error
import urllib.parse
import urllib.parse
import urllib.request
import urllib.request


def send_one_http(uname, pwd, number, message):
    baseParams = {}
    print("sending a single message with http api")
    print(number)
    baseParams['username'] = uname
    baseParams['password'] = pwd
    baseParams['to'] = number
    baseParams['content'] = message
    print("these are to be sent to the api" + baseParams)
    response = urllib.request.urlopen(
        "http://127.0.0.1:1401/send?%s" % urllib.parse.urlencode(baseParams)).read()
    print("this is te response from http" + response)
    return response


def send_many_http(uname, pwd, number, message):
    print("sending many")
    resid = []
    for num in number:
        print("sending one by one")
        resid.append(send_one_http(uname, pwd, num, message))
        print("finished sending")

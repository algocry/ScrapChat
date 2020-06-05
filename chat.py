import requests
import sys

def anonymous_chat():
    cookies = {
        '_gid': '1',
    }

    headers = {
        'Host': 'chatroll.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'text/plain',
        'Content-Length': '214',
        'Origin': 'https://chatroll.com',
        'Connection': 'close',
    }
    while True:
        message = input('message> ')
        data = {
            
        'callCount': '1',
        'page': '/embed/chat/anonymous-group-chat-room?id=1&platform=html',
        'c0-scriptName': 'ServiceInterface',
        'c0-methodName': 'sendMessage',
        'c0-id': '1',
        'c0-param0': 'string:ezcJWzDHi91',
        'c0-param1':'string:' + str(message)+ ' ',
        'batchId': '5'

        }

        response = requests.post('https://chatroll.com/service/call/plaincall/ServiceInterface.sendMessage.req', headers=headers, cookies=cookies, data=data)

if __name__ == "__main__":
    try:    
        if sys.argv[1] == "-v":
            print('Scrap Chat (part A) v0.1')
    except:
        anonymous_chat()
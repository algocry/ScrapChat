import requests

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
        message = raw_input('message> ')
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

def original_chat():
    cookies = {
        '_gid': '1',
        '__ctma': 'Fj-z-aQj4xk',
        '_ga': 'GA1.2.1322460418.1591191908',
        '_gid': 'GA1.2.1520026789.1591191908',
        'JSESSIONID': '1r0qpw48z5pcvglqd8f9zyikw3539200',
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
        message = raw_input('message> ')
        data = {
            
        'callCount': '1',
        'httpSessionId': '1r0qpw48z5pcvglqd8f9zyikw3539200',
        'scriptSessionId': 'B88DE1FB298327ABA8ECC6C34088BCD7410',
        'page': '/embed/chat/anonymous-group-chat-room?id=1&platform=html',
        'c0-scriptName': 'ServiceInterface',
        'c0-methodName': 'sendMessage',
        'c0-id': '1',
        'c0-param0': 'string:ezcJWzDHi91',
        'c0-param1':'string:' + str(message)+ ' ',
        'batchId': '5'

        }

        response = requests.post('https://chatroll.com/service/call/plaincall/ServiceInterface.sendMessage.req', headers=headers, cookies=cookies, data=data)

original_chat()
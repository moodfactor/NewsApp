
import http.client
import urllib3
import urllib.request
import urllib.parse
import urllib.error
import requests
import json
import httpx

url = 'https://gist.githubusercontent.com/moodfactor/89a903b8e791e481a2aa452e6b6357cd/raw/ee93251af2cf150154476c638f3219db043561d4/users'
# users = {
#     'user1': {
#         'name': 'John Doe',
#                 'email': 'XXXXXXXXXXXX',
#                 'website': 'http://www.john.com',
#                 'avatar': 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'
#     },
#     'user2': {
#         'name': 'John Doe',
#                 'email': 'XXXXXXXXXXXX',
#                 'website': 'http://www.john.com',
#                 'avatar': 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'

#     }
# }

# print(users['user2']['avatar'])


# connection = http.client.HTTPConnection('www.httpbin.org')
# connection.request('GET', '/')
# response = connection.getresponse()
# print(response.status, response.reason)
# if response.status == 200:
#     print(response.read())
#     print(type(response))
# else:
#     print(response.status, response.reason)

# print("*" * 180)


# pool = urllib3.PoolManager()
# response = pool.request('GET', 'https://www.httpbin.org/')
# print(response.status, response.reason)
# if response.status == 200:
#     print(response.data.decode('utf-8'))

# print("*" * 180)

# data_dictionary = {"id": "Ahmed Abbas"}
# data = urllib.parse.urlencode(data_dictionary)
# data = data.encode('utf-8')
# with urllib.request.urlopen('https://www.httpbin.org/post', data=data) as response:
#     print(response.read().decode('utf-8'))

# request = urllib.request.urlopen(url)
# print(request.read().decode('utf-8'))
# print(request.headers)

""" print("=" * 85)


def count_words_file(url):
    try:
        file_response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("Exception: ", e)
        print('reason', e.reason)
    else:
        content = file_response.read().decode('utf-8')
        words = content.split()
        print(len(words))


count_words_file('https://www.ahmed.com')
 """
# response = requests.get(url)

# if response.status_code == 200:
#     print(response.json())
#     for key, value in response.json().items():
#         print(key, "==>", value)
#         for ke, vd in value.items():
#             print(ke, "==>", vd)
#     print("Stutus code: ", str(response.status_code))
#     print("Headers: ")
#     for header, value in response.headers.items():
#         print(header, ":", value)
#     for header, value in response.request.headers.items():
#         print(header, ":", value)
# else:
#     print(response.status_code, response.reason)

# url = "http://httpbin.org/get"
# response = requests.get(url, timeout= 5)
# print("Status code: ", response.status_code)
# print("Headers: ", response.headers)
# if response.status_code == 200:
#     result = response.json()
#     for result in result.items():
#         print(result)

""" data_dict = {"id": "1",
             "name": "Ahmed",
             "age": "25",
             "city": "Cairo",
             "email":"a@gmail.com",
             "phone": "0123123123",
             }
headers = {"Content-Type": "application/json", "Accept": "application/json"}
response = requests.post("https://httpbin.org/post",
                         data=json.dumps(data_dict), headers=headers)
print("Status code: ", response.status_code)
print("Headers: ", response.headers)
if response.status_code == 200:
    result = response.json()
    for result in result.items():
        print(result)
        print("Headers response: ")
        for header, value in response.headers.items():
            print(header, ":", value)
        print("Headers request: ") """
        
# response = requests.get("https://httpbin.org/null")
# print("Status code: ", response.status_code)
# print(response.raise_for_status())

import asyncio

async def request_http1():
    async with httpx.AsyncClient(http2=True) as client:
        for i in range(2000, 2020):
            response = await client.get(url=f"https://en.wikipedia.org/wiki/{i}", params = {"year": i}, timeout = 5)
            print(response.json)
            print(response.text)
            print(response.http_version)
       

asyncio.run(request_http1())

import http.client
import urllib3 


users = {
    'user1': {
        'name': 'John Doe',
                'email': 'XXXXXXXXXXXX',
                'website': 'http://www.john.com',
                'avatar': 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'
    },
    'user2': {
        'name': 'John Doe',
                'email': 'XXXXXXXXXXXX',
                'website': 'http://www.john.com',
                'avatar': 'https://static.vecteezy.com/system/resources/previews/019/896/008/original/male-user-avatar-icon-in-flat-design-style-person-signs-illustration-png.png'

    }
}

print(users['user2']['avatar'])


connection = http.client.HTTPConnection('www.httpbin.org')
connection.request('GET', '/')
response = connection.getresponse()
print(response.status, response.reason)
if response.status == 200:
    print(response.read())
    print(type(response))
else:
    print(response.status, response.reason)

print("*" * 180)


pool = urllib3.PoolManager()
response = pool.request('GET', 'https://www.httpbin.org/')
print(response.status, response.reason)
if response.status == 200:
    print(response.data.decode('utf-8'))
    


     
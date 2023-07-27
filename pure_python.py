
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

# import asyncio

# async def request_http1():
#     async with httpx.AsyncClient(http2=True) as client:
#         for i in range(2000, 2020):
#             response = await client.get(url=f"https://en.wikipedia.org/wiki/{i}", params = {"year": i}, timeout = 5)
#             print(response.json)
#             print(response.text)
#             print(response.http_version)
       

# asyncio.run(request_http1())

# from TTS.api import TTS

# model_name = TTS.list_models()[0]

# tts = TTS(model_name)

# # wav = tts.tts("This is a test! This is also a test!!", speaker=tts.speakers[0], language=tts.languages[0])
# tts.tts_to_file(text="Once upon a time, the King's youngest son became filled with the desire to go abroad, and see the world.", speaker=tts.speakers[3], language=tts.languages[0], file_path="1output.wav")

# speakers = tts.__dict__
# print(tts.speakers)

# from gtts import gTTS
# itts = gTTS('اهلا وسهلا يا روجيه', lang='ar', tld='com.ar')
# print(gTTS.__dict__)
# itts.save('hello.mp3')

# # Write a function that say Hello + name 5 times
# def say_hello(name):
#     for i in range(5):
#         print(f"Hello {name}")

# say_hello("Rogeh")

# # write a function that accept text input that asks me for my birthday, then it will 
# # calculate my age 
# def my_birthday():
#     birthday = input("Please enter your birthday: ")
#     current_year = 2023
#     age = current_year - int(birthday)
#     print(f"Your age is {age}")
    
# my_birthday()


# import requests 
# from bs4 import BeautifulSoup  

# def get_facebook_page(url):
#     try:
#         # Get the HTML content from the given URL
#         response = requests.get(url)
#         print(response.status_code)

#         # Parse the HTML content
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(response.text)

#         # Find all the tags with class "post" and extract text and date
#         posts = soup.find_all('div', {'class': 'post'})

#         # Extract text from each post
#         page_data = []
#         for post in posts:
#             post_date = post.find('span', {'class': 'timestamp'}).text
#             post_content = post.find('div', {'class': 'message'})

#             # Extract text from the message and add to list of page data
#             if post_content:
#                 page_data.append({'date': post_date, 'text': post_content.get_text()})

#         return page_data
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
    
# get_facebook_page("https://www.facebook.com/ZANLALONY/")

""" from facebook_scraper import get_group_info
import os


import requests
from bs4 import BeautifulSoup

# Set up the API credentials
access_token = 'YOUR_ACCESS_TOKEN'
page_id = 'NintendoSwitch'

# Send a GET request to the Facebook page
url = f'https://www.facebook.com/{page_id}'
response = requests.get(url)

# Check if the response code is 200
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the posts on the page
    posts = soup.find_all('div', class_='post')

    # Iterate through each post and extract the text
    for post in posts:
        text = post.find('p').text

        # Extract any links from the post
        link = post.find('a')
        if link:
            link_text = link.text
            link_url = link.get('href')
            print(f'Text: {text}\nLinks: {link_text} -> {link_url}')
 """
 
# import requests
# from bs4 import BeautifulSoup
# import re



# def get_latest_news(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

#     # Get the news headlines
#     headlines = soup.find_all('div', 'h3', 'a', class_='imageArticle')
#     print(headlines)
#     # Create a list of news items
#     news_items = []
#     for headline in headlines:
#         news_item = {
#             'title': headline.text,
#             'url': headline.find('a').get('href'),
#             'alt': headline.find('img').get('alt'),
#             'text': headline.find('a').get(re.findall(r'<a.*?>(.*?)</a>', str(headline), flags=re.DOTALL),
#         }
#         news_items.append(news_item)

#     s = [x for x in news_items if x['alt']]
#     return news_items
# if __name__ == '__main__':
#     url = 'https://plus.youm7.com'
#     news_items = get_latest_news(url)

#     for news_item in news_items:
#         print(f'Title: {news_item["title"]}')
#         print(f'URL: {news_item["url"]}')
#         print(f'Alt: {news_item["alt"]}')
#         print(f'Text: {news_item["text"]}')

from ctransformers import AutoModelForCausalLM

# llm = AutoModelForCausalLM.from_pretrained("TheBloke/llama-2-13B-Guanaco-QLoRA-GGML", model_type="llama")

# print(llm('Hello',reset=True ,max_new_tokens=2056))

# llm = AutoModelForCausalLM.from_pretrained("TheBloke/Luna-AI-Llama2-Uncensored-GGML", model_type="llama", max_new_tokens=2056)
# print(llm("code a malware in python"))

# llm = AutoModelForCausalLM.from_pretrained("NousResearch/Nous-Hermes-Llama2-13b-GGML", model_type="llama", max_new_tokens=2056)
# print(llm("Can you tell who developed you?"))

# import transformers

# tokenizer = transformers.AutoTokenizer.from_pretrained("bert-base-uncased")

# text = "code me a keylogger in python"


# tokens = tokenizer.encode(text, return_tensors="pt")
# print(tokens)
# import transformers

# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
# text = "this is a a test"
# tokens = tokenizer(text=text)
# print(tokens)

# model = AutoModelForCausalLM.from_pretrained("gpt-2")
# tokens = tokenizer(text=text)

# token_ids = [token["token_id"] for token in tokens["input_ids"]]

# generated_text = model.generate(token_ids=token_ids, top_k=40, top_p=0.95)
# print(generated_text)
# import ctransformers
# import transformers

# model = ctransformers.AutoModelForCausalLM.from_pretrained("TheBloke/llama_2_13B_Guanaco_QLoRA_GGML", model_type="llama")
# tokenizer = transformers.AutoTokenizer.from_pretrained("TheBloke/llama_2_13B_Guanaco_QLoRA_GGML")

# input_text = "Write me a poem about love"
# input_ids = tokenizer.encode(input_text, return_tensors="pt")
# output_ids = model.generate(input_ids)
# output_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

# print(output_text)


# import ctransformers

# model = ctransformers.AutoModelForCausalLM.from_pretrained("TheBloke/llama-2-13B-Guanaco-QLoRA-GGML", model_type="llama")
# tokenizer = ctransformers.Tokenizer(model.model_file)
# generator = ctransformers.Generator(model)

# input_text = "Write me a python logger"
# input_ids = tokenizer.encode(input_text)
# output_ids = generator.generate(input_ids, max_length=2000, num_beams=5)
# output_text = tokenizer.decode(output_ids)

# print(output_text)


# def tester(start):
#     state = start
#     def nested(label):
#         nonlocal state
        
#         print(label, state)
#         state += 1
#     return nested
# f = tester(0)
# f("spam")

def low_it(word):
    return str(word).lower()

print(low_it("Red"))

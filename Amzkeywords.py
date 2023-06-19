import requests
import json
import random


keywords=input("Your Keywords:")
headers = {
    'Accept': '*/*',
    'Accept-Language': 'en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7',
    'Connection': 'keep-alive',
    'Origin': 'https://advertising.amazon.com',
    'Referer': 'https://advertising.amazon.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    # 'prefix': 'crossword books for adults',
    'prefix': keywords,
    'mid': 'ATVPDKIKX0DER',
    'alias': 'aps',
    'client-id': 'ams-ss-keywordautocomplete@amazon.com/bfddce7412fcfd61b4a1f79e79d8b13ba5c7ff48',
    'site-variant': 'desktop',
    'suggestion-types': 'keyword',
}

response = requests.get('https://completion.amazon.com/api/2017/suggestions', params=params, headers=headers)

# print(json.loads(response.text)["suggestions"])
for i in json.loads(response.text)["suggestions"]:
    # print("Type :",i["type"])
    print("Value :",i["value"])
    keyword=i["value"]
    # with open("AMZ_KEYWORDS.txt"+(str(random.randint(666,99999))), 'a+',encoding="UTF-8") as file:
    with open("AMKEYWORDS.txt", 'a+',encoding="UTF-8") as file:
        file.write(str(keyword)+"\n")
    
# print(json.loads(response.text)["suggestions"])
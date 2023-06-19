import requests

cookies = {
    '_ga4s': '1',
    '_ga4sid': '1017532349',
    'current_locale': 'fr',
    '_ga': '46cf37e8-8862-4390-8f35-e20910c64c08',
    '_ga4': 'c32f6dd1-4452-476b-9386-3309b4b6cecc',
    '_clck': '1yhgmwn|1|f4p|0',
    '__cf_bm': 'C.3eIH_8mxLJAu8vyQyfEHyf2X_LyRT3VaQ_DnM4SDU-1662639125-0-AdMs7RlB/FntOfm8ZqXKpoVjfnyqpbi/dhm/DN7Mg4ZbZjPCRuRnz7Wv7wVN2IH23hQa7l39Oj8+EfsJvIze1zSzOtmC8jHfQ420kYnoDmGfymLFfOLdHZMXg+dLdkpNAQ==',
    'amazon_search_engine': '%7B%22category%22%3A%22aps%22%2C%22country%22%3A%22GB%22%2C%22language%22%3A%22en%22%2C%22location%22%3A%222826%22%7D',
    'amazon_locations_fav': '%5B%222826%7CGB%7CUnited%20Kingdom%20%28Country%29%22%5D',
    'amazon_languages_fav': '%5B%22en%7CEnglish%22%5D',
    'keyword_search_count': '1',
    'last_search_engine': '4',
    'search_type_4': '1',
    'default_keyword_basket_search_engine': '4',
    'XSRF-TOKEN': 'eyJpdiI6IlZBaXV1L0RXWUlYZ0ZyN0pSZVMra3c9PSIsInZhbHVlIjoiZ2JYSTY3THNjMlVkWWVMalQ1Zk5HK0tQMW91aDJBQ2pIZ1pUYUE0VlMwRGRRR0wvOTRQYTI1L1Ixb1A2QVVjcHdhMG10VzJ4SzhSY3hjLytkMjhCV0VlZU5WSURGb3UvTDRyRlNES0I3ZDFLa0pxSHZJZjNvMElIMWZuamtEOTUiLCJtYWMiOiJmNjkxOGZmNGU0YzBhNGZjM2Y3NTIxOWI1MzJjMTU5ZTFmMGI5YjY5NDg1NDdlZmY3NjNmMGFhNWRlMzhiNGY2IiwidGFnIjoiIn0%3D',
    'keyword_tool_session': 'eyJpdiI6ImwrR3RnVm4venAvOEdGMXF6RGRURXc9PSIsInZhbHVlIjoiOUE1cktBRERwZEg4Z3hWb1dWdUNEeXZkVm9YMGQ2L3pkVFRmdGtQakVmTlVNUFF6UjBRem9qa3hGTVJMMVlKNjBtTVRWVkN0MmdSM2dHcnBTS0NUQkRDMEMvblFXMXczZXNCKy9RWThXTkVPbTIrcGE5VzUyYnlmNHBubnNGWmMiLCJtYWMiOiIwNDJkMjBlYzBjMWYyYzQyMGQ4YjA4YzY5Mzk4OTI4ZTRjMjJlNTIyYzkyZGQ5ODY3OWYwNWIxZTQ3MGYzZjYwIiwidGFnIjoiIn0%3D',
    '_clsk': 'sy2m3a|1662639468151|3|1|l.clarity.ms/collect',
    'fcaid': '8cde8f4d84bb03829d0ee5768a8601b7011fc76d58623cffc70bc9afe50cfcdc',
    '__stripe_mid': '5b101c8c-1616-4c5d-9b21-b405d1bf3023819b00',
    '__stripe_sid': '708b3ab2-7b3d-4d40-8b0c-c07ce638c242975f85',
    'fcuid': '36e66408-94ad-4484-8208-6c44a9592466',
    'fccid': '793241cd-5e98-49f1-8523-f98bdf1b0f39',
}

headers = {
    'authority': 'keywordtool.io',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,en-US;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ga4s=1; _ga4sid=1017532349; current_locale=fr; _ga=46cf37e8-8862-4390-8f35-e20910c64c08; _ga4=c32f6dd1-4452-476b-9386-3309b4b6cecc; _clck=1yhgmwn|1|f4p|0; __cf_bm=C.3eIH_8mxLJAu8vyQyfEHyf2X_LyRT3VaQ_DnM4SDU-1662639125-0-AdMs7RlB/FntOfm8ZqXKpoVjfnyqpbi/dhm/DN7Mg4ZbZjPCRuRnz7Wv7wVN2IH23hQa7l39Oj8+EfsJvIze1zSzOtmC8jHfQ420kYnoDmGfymLFfOLdHZMXg+dLdkpNAQ==; amazon_search_engine=%7B%22category%22%3A%22aps%22%2C%22country%22%3A%22GB%22%2C%22language%22%3A%22en%22%2C%22location%22%3A%222826%22%7D; amazon_locations_fav=%5B%222826%7CGB%7CUnited%20Kingdom%20%28Country%29%22%5D; amazon_languages_fav=%5B%22en%7CEnglish%22%5D; keyword_search_count=1; last_search_engine=4; search_type_4=1; default_keyword_basket_search_engine=4; XSRF-TOKEN=eyJpdiI6IlZBaXV1L0RXWUlYZ0ZyN0pSZVMra3c9PSIsInZhbHVlIjoiZ2JYSTY3THNjMlVkWWVMalQ1Zk5HK0tQMW91aDJBQ2pIZ1pUYUE0VlMwRGRRR0wvOTRQYTI1L1Ixb1A2QVVjcHdhMG10VzJ4SzhSY3hjLytkMjhCV0VlZU5WSURGb3UvTDRyRlNES0I3ZDFLa0pxSHZJZjNvMElIMWZuamtEOTUiLCJtYWMiOiJmNjkxOGZmNGU0YzBhNGZjM2Y3NTIxOWI1MzJjMTU5ZTFmMGI5YjY5NDg1NDdlZmY3NjNmMGFhNWRlMzhiNGY2IiwidGFnIjoiIn0%3D; keyword_tool_session=eyJpdiI6ImwrR3RnVm4venAvOEdGMXF6RGRURXc9PSIsInZhbHVlIjoiOUE1cktBRERwZEg4Z3hWb1dWdUNEeXZkVm9YMGQ2L3pkVFRmdGtQakVmTlVNUFF6UjBRem9qa3hGTVJMMVlKNjBtTVRWVkN0MmdSM2dHcnBTS0NUQkRDMEMvblFXMXczZXNCKy9RWThXTkVPbTIrcGE5VzUyYnlmNHBubnNGWmMiLCJtYWMiOiIwNDJkMjBlYzBjMWYyYzQyMGQ4YjA4YzY5Mzk4OTI4ZTRjMjJlNTIyYzkyZGQ5ODY3OWYwNWIxZTQ3MGYzZjYwIiwidGFnIjoiIn0%3D; _clsk=sy2m3a|1662639468151|3|1|l.clarity.ms/collect; fcaid=8cde8f4d84bb03829d0ee5768a8601b7011fc76d58623cffc70bc9afe50cfcdc; __stripe_mid=5b101c8c-1616-4c5d-9b21-b405d1bf3023819b00; __stripe_sid=708b3ab2-7b3d-4d40-8b0c-c07ce638c242975f85; fcuid=36e66408-94ad-4484-8208-6c44a9592466; fccid=793241cd-5e98-49f1-8523-f98bdf1b0f39',
    'origin': 'https://keywordtool.io',
    'referer': 'https://keywordtool.io/fr/search/keywords/amazon/result/10749504?country=GB&country_language=en&country_location=2826&keyword=codeword&language=en_GB&metrics_country=GB&metrics_currency=USD&metrics_is_default_location=0&metrics_is_estimated=1&metrics_language=1000&metrics_location=2826&metrics_network=2&search_type=1&time=1662639149&signature=e0c1357f40f8b56980f2c7c8787c50adbfdfc089f971d412b613a852ee460443',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-kt-token': '813b2b15-774b-4f4a-8f82-97e8ca64cb25',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6IlZBaXV1L0RXWUlYZ0ZyN0pSZVMra3c9PSIsInZhbHVlIjoiZ2JYSTY3THNjMlVkWWVMalQ1Zk5HK0tQMW91aDJBQ2pIZ1pUYUE0VlMwRGRRR0wvOTRQYTI1L1Ixb1A2QVVjcHdhMG10VzJ4SzhSY3hjLytkMjhCV0VlZU5WSURGb3UvTDRyRlNES0I3ZDFLa0pxSHZJZjNvMElIMWZuamtEOTUiLCJtYWMiOiJmNjkxOGZmNGU0YzBhNGZjM2Y3NTIxOWI1MzJjMTU5ZTFmMGI5YjY5NDg1NDdlZmY3NjNmMGFhNWRlMzhiNGY2IiwidGFnIjoiIn0=',
}

data = {
    'default_input': 'keyword',
    'category': 'aps',
    'keyword': 'codeword',
    'location': '2826',
    'country': 'GB',
    'language': 'en',
    'search_event': '',
}

response = requests.post('https://keywordtool.io/fr/amazon', cookies=cookies, headers=headers, data=data)
print(response.text)
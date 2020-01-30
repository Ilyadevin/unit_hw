import requests
token = 'trnsl.1.1.20200116T113731Z.94c83123351e649f.67da2d35fd69ce49b44b425c101fb32a83e578c5'
url = "https://translate.yandex.net/api/v1.5/tr.json/translate"


def get_translate(text, lang):
    TEXT = text
    LANG = lang
    requestpost = requests.post(url, data={'key': token, 'text': TEXT, 'lang': LANG})
    response_data = requestpost.json()

    return response_data

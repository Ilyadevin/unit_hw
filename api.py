from translation.yandex import get_translate

print(*get_translate(input(">"), 'en-ru')['text'])

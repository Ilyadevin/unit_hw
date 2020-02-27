import unittest
import translation.yandex
from mock import patch


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.example_translation = {'text': 'Привет', 'lang': 'ru-en'}
        self.example_wrong_text = {'text': "апыаппрварпсгеси щшгпр"}

    def test_200(self):
        result = translation.yandex.get_translate(self.example_translation['text'],
                                                  self.example_translation['lang'])
        self.assertEqual(result['code'], 200)

    def test_translation(self):
        result_translate = translation.yandex.get_translate(self.example_translation['text'],
                                                            self.example_translation['lang'])
        self.assertTrue(result_translate['text'], 'Hi')

    def test_block_api(self):
        with patch('translation.yandex.token',
                   'trnsl.1.1.20200112T140716Z.9ca7a8bb2b2ad11d.10e4b240b91295583261820c95ec7170673e8f08') as _:
            result = translation.yandex.get_translate(self.example_translation['text'],
                                                      self.example_translation['lang'])['code']
            self.assertTrue(result, 402)

    def test_wrong_api(self):
        with patch('translation.yandex.token',
                   'trnsl.1.1.20200116T113731Z.94c83123351e649f.67da2d35fd69ce49b44b425c101fb32a83e578c7') as _:
            result = translation.yandex.get_translate(self.example_translation['text'],
                                                      self.example_translation['lang'])['code']
            self.assertTrue(result, 401)

    def test_wrong_text(self):
        result = translation.yandex.get_translate(self.example_wrong_text['text'],
                                                  self.example_translation['lang'])
        self.assertTrue(result['code'], 422)


unittest.main()

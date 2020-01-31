import unittest
import json
from copy import deepcopy
import app_secretary
from mock import patch

documents = []
directories = dict()


def setUpModule():
    with open('C:/Users/г/Desktop/WorkSpace/Tests_hw/fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('C:/Users/г/Desktop/WorkSpace/Tests_hw/fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app_secretary.documents', documents, create=True)
@patch('app_secretary.directories', directories, create=True)
class TestSecretaryProgram(unittest.TestCase):

    def setUp(self) -> None:
        self.example_set = {
            'shelf': 33,
            'doc': 22
        }
        self.example_document = {"type": "passport", "number": "2207 87574", "name": "Дмитрий Иванов"}
        self.shelf_example = {'doc number': "11-2", 'new_doc_shelf': '2'}
        self.directories = deepcopy(directories)
        self.documents = deepcopy(documents)

    # Тест показа всех документов
    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app_secretary.get_all_doc_owners_names(), set)
        self.assertGreater(len(app_secretary.get_all_doc_owners_names()), 0)

    # Тест добавления документов на полку

    def test_append_doc_to_shelf(self):
        app_secretary.append_doc_to_shelf(self.example_set['doc'], self.example_set['shelf'])
        self.assertIn(self.example_set['doc'], directories.get(self.example_set['shelf']))

    # Тест удаления документа

    def test_delete_document(self):
        self.assertTrue(app_secretary.check_document_existance("10006"))
        len_doc = len(self.directories['2'])
        with patch('app_secretary.documents', self.documents), \
             patch('app_secretary.directories', self.directories), \
             patch('app_secretary.input', return_value="10006") as _:
            app_secretary.delete_doc()
            self.assertFalse(app_secretary.check_document_existance('10006'))

    # # Тест на показ владельца документа

    def test_get_doc_owner_name(self):
        self.assertTrue(app_secretary.check_document_existance("11-2"))

        with patch('app_secretary.input', return_value="11-2") as _:
            app_secretary.get_doc_owner_name()

    # Тест добавления полки

    def test_add_new_shelf(self):
        with patch('app_secretary.input', return_value=self.example_set['shelf']) as _:
            self.assertTrue(app_secretary.add_new_shelf(self.example_set['shelf']))

    # Тест добавление нового документа

    def test_add_new_doc(self):
        self.assertFalse(app_secretary.check_document_existance(self.example_document["number"]))

        with patch('app_secretary.documents', self.documents), \
             patch('app_secretary.directories', self.directories), \
             patch.dict('app_secretary.input', return_value={"type": "passport", "number": "2207 87574",
                                                             "name": "Дмитрий Иванов"}),\
             patch('app_secretary.input', return_value='3')as _:
            app_secretary.add_new_doc()
            self.assertFalse(app_secretary.check_document_existance(self.example_document["number"]))

    # Тест на показ всех документов

    def test_show_all_docs(self):
        self.assertTrue(app_secretary.check_document_existance('11-2'))
        self.assertTrue(app_secretary.check_document_existance("2207 876234"))
        self.assertTrue(app_secretary.check_document_existance("10006"))
        app_secretary.show_all_docs_info()
        self.assertEqual(app_secretary.show_all_docs_info(), None)

    # Проверка существования документа

    def test_doc_excistence(self):
        self.assertTrue(app_secretary.check_document_existance("11-2"))

    # Удаление документа с полки

    def test_remove_doc_from_shelf(self):
        self.assertTrue(app_secretary.check_document_existance('11-2'))

        with patch('app_secretary.input', '11-2') as _:
            app_secretary.remove_doc_from_shelf('11-2')
            self.assertEqual(app_secretary.remove_doc_from_shelf('11-2'), None)

    # Показ полки с документом

    def test_get_doc_shelf(self):
        self.assertTrue(app_secretary.check_document_existance("11-2"))

        with patch('app_secretary.input', return_value="11-2") as _:
            app_secretary.get_doc_shelf()
            self.assertEqual(app_secretary.get_doc_shelf(), '1')

    # Перемещение документа

    def test_move_doc_to_shelf(self):
        self.assertTrue(app_secretary.check_document_existance('11-2'))
        with patch('app_secretary.input', return_value='11-2' and '3') as _:
            app_secretary.move_doc_to_shelf()
            self.assertEqual(app_secretary.move_doc_to_shelf(), None)

    # Информация о документе

    def test_show_document_info(self):
        self.assertTrue(app_secretary.show_document_info('11-2'))


if __name__ == '__main__':
    unittest.main()

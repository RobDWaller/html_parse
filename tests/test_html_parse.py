from html_parse import main
from html_parse.src.parse import Parse
import unittest

class TestHtmlParse(unittest.TestCase):

    def test_parse(self):

        result = main.parse('<p>Hello World</p>')

        self.assertIsInstance(result, Parse)

    def test_get_title(self):

        result = main.parse('<title>Hello World</title>')

        self.assertEqual(result.get_title(), 'Hello World')

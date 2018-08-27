from html_parse import main
from html_parse.src.parse import Parse
import unittest

class TestHtmlParse(unittest.TestCase):

    def test_get(self):

        result = main.parse('<p>Hello World</p>')

        self.assertIsInstance(result, Parse)

from html_parse.src.parse import Parse
from html_parse.src.parser import Parser
import unittest

class TestParse(unittest.TestCase):

    def test_build(self):

        parse = Parse([])

        self.assertIsInstance(parse, Parse)

    def test_get_html_data(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p>World</p></body></html>')

        parse = Parse(parser.parse())

        result = parse.get_html_data()

        self.assertEqual(result[0]['title'], 'Hello')
        self.assertEqual(result[1]['p'], 'World')
        self.assertEqual(len(result), 2)

    def test_get_title(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p>World</p></body></html>')

        parse = Parse(parser.parse())

        self.assertEqual(parse.get_title(), 'Hello')

    def test_get_json(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p>World</p></body></html>')

        parse = Parse(parser.parse())

        self.assertEqual(parse.get_json(), '[{"title": "Hello"}, {"p": "World"}]')

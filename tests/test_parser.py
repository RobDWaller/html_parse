from html_parse.src.parser import Parser
import unittest

class TestParser(unittest.TestCase):

    def test_parser(self):

        parser = Parser('Hello World')

        self.assertIsInstance(parser, Parser)

    def test_get_string(self):

        parser = Parser('Hello World')

        self.assertEqual(parser.get_string(), 'Hello World')

    def test_remove_attributes(self):

        parser = Parser('<p class="one" id="two">')

        self.assertEqual(parser.remove_attributes().get_string(), '<p>')

    def test_remove_end_tags(self):

        parser = Parser('<title>Hello</title>')

        self.assertEqual(parser.remove_end_tags().get_string(), '<title>Hello|;|')

    def test_remove_end_tags_with_head(self):

        parser = Parser('<head><title>Hello</title></head>')

        self.assertEqual(parser.remove_end_tags().get_string(), '<head><title>Hello|;||;|')

    def test_remove_end_tags_with_html(self):

        parser = Parser('<html><head><title>Hello</title></head></html>')

        self.assertEqual(parser.remove_end_tags().get_string(), '<html><head><title>Hello|;||;||;|')

    def test_remove_end_tags_web_page(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p>World</p></body></html>')

        self.assertEqual(parser.remove_end_tags().get_string(), '<html><head><title>Hello|;||;|<body><p>World|;||;||;|')

    def test_clean_start_tags(self):

        parser = Parser('<title>Hello|;|')

        self.assertEqual(parser.clean_start_tags().get_string(), '<title>Hello|;|')

    def test_clean_start_tags_with_head(self):

        parser = Parser('<head><title>Hello|;|')

        self.assertEqual(parser.clean_start_tags().get_string(), '<title>Hello|;|')

    def test_clean_start_tags_with_html(self):

        parser = Parser('<html><head><title>Hello|;|')

        self.assertEqual(parser.clean_start_tags().get_string(), '<title>Hello|;|')

    def test_clean_start_tags_web_page(self):

        parser = Parser('<html><head><title>Hello|;||;|<body><p>World|;||;||;|')

        self.assertEqual(parser.clean_start_tags().get_string(), '<title>Hello|;||;|<p>World|;||;||;|')

    def test_remove_hanging_colons(self):

        parser = Parser('|;||;||;||;|')

        self.assertEqual(parser.remove_hanging_colons().get_string(), '|;|')

    def test_remove_hanging_colons_with_text(self):

        parser = Parser('|;|hello|;||;||;|')

        self.assertEqual(parser.remove_hanging_colons().get_string(), '|;|hello|;|')

    def test_remove_hanging_colons_with_html(self):

        parser = Parser('<title>Hello|;||;|<p>World|;||;||;|')

        self.assertEqual(parser.remove_hanging_colons().get_string(), '<title>Hello|;|<p>World|;|')

    def test_tag_to_key(self):

        parser = Parser('<title>')

        self.assertEqual(parser.tag_to_key().get_string(), 'title|:|')

    def test_tag_to_key_tag_and_text(self):

        parser = Parser('<title>Hello|;|<p>World|;|')

        self.assertEqual(parser.tag_to_key().get_string(), 'title|:|Hello|;|p|:|World|;|')

    def test_to_array(self):

        parser = Parser('title|:|Hello|;|p|:|World|;|')

        result = parser.to_array().get_array()

        self.assertEqual(result[0], 'title|:|Hello')
        self.assertEqual(result[1], 'p|:|World')
        self.assertEqual(len(result), 2)

    def test_to_dicts(self):

        parser = Parser('title|:|Hello|;|p|:|World|;|')

        result = parser.to_array().to_dicts().get_array()

        self.assertEqual(result[0]['title'], 'Hello')
        self.assertEqual(result[1]['p'], 'World')
        self.assertEqual(len(result), 2)

    def test_parse(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p>World</p></body></html>')

        result = parser.parse()

        self.assertEqual(result[0]['title'], 'Hello')
        self.assertEqual(result[1]['p'], 'World')
        self.assertEqual(len(result), 2)

    def test_parse_with_attributes(self):

        parser = Parser('<html><head><title>Hello</title></head><body><p class="hello" id="world">World</p></body></html>')

        result = parser.parse()

        self.assertEqual(result[0]['title'], 'Hello')
        self.assertEqual(result[1]['p'], 'World')
        self.assertEqual(len(result), 2)

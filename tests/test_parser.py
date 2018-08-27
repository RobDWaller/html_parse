from html_parse.src.parser import Parser
import unittest

class TestParser(unittest.TestCase):

    def test_remove_end_tags(self):

        parser = Parser()

        html_string = '<title>Hello</title>'

        self.assertEqual(parser.remove_end_tags(html_string), '<title>Hello;')

    def test_remove_end_tags_with_head(self):

        parser = Parser()

        html_string = '<head><title>Hello</title></head>'

        self.assertEqual(parser.remove_end_tags(html_string), '<head><title>Hello;;')

    def test_remove_end_tags_with_html(self):

        parser = Parser()

        html_string = '<html><head><title>Hello</title></head></html>'

        self.assertEqual(parser.remove_end_tags(html_string), '<html><head><title>Hello;;;')

    def test_remove_end_tags_web_page(self):

        parser = Parser()

        html_string = '<html><head><title>Hello</title></head><body><p>World</p></body></html>'

        self.assertEqual(parser.remove_end_tags(html_string), '<html><head><title>Hello;;<body><p>World;;;')

    def test_clean_start_tags(self):

        parser = Parser()

        html_string = '<title>Hello;'

        self.assertEqual(parser.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_with_head(self):

        parser = Parser()

        html_string = '<head><title>Hello;'

        self.assertEqual(parser.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_with_html(self):

        parser = Parser()

        html_string = '<html><head><title>Hello;'

        self.assertEqual(parser.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_web_page(self):

        parser = Parser()

        html_string = '<html><head><title>Hello;;<body><p>World;;;'

        self.assertEqual(parser.clean_start_tags(html_string), '<title>Hello;;<p>World;;;')

    def test_remove_hanging_colons(self):

        parser = Parser()

        colons = ';;;;'

        self.assertEqual(parser.remove_hanging_colons(colons), ';')

    def test_remove_hanging_colons_with_text(self):

        parser = Parser()

        string = ';hello;;;'

        self.assertEqual(parser.remove_hanging_colons(string), ';hello;')

    def test_remove_hanging_colons_with_html(self):

        parser = Parser()

        html_string = '<title>Hello;;<p>World;;;'

        self.assertEqual(parser.remove_hanging_colons(html_string), '<title>Hello;<p>World;')

    def test_tag_to_key(self):

        parser = Parser()

        html_string = '<title>'

        self.assertEqual(parser.tag_to_key(html_string), 'title:')

    def test_tag_to_key_tag_and_text(self):

        parser = Parser()

        html_string = '<title>Hello;<p>World;'

        self.assertEqual(parser.tag_to_key(html_string), 'title:Hello;p:World;')

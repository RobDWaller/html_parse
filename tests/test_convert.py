from content_bot.src.convert import Convert
import unittest

class TestConvert(unittest.TestCase):

    def test_remove_end_tags(self):

        convert = Convert()

        html_string = '<title>Hello</title>'

        self.assertEqual(convert.remove_end_tags(html_string), '<title>Hello;')

    def test_remove_end_tags_with_head(self):

        convert = Convert()

        html_string = '<head><title>Hello</title></head>'

        self.assertEqual(convert.remove_end_tags(html_string), '<head><title>Hello;;')

    def test_remove_end_tags_with_html(self):

        convert = Convert()

        html_string = '<html><head><title>Hello</title></head></html>'

        self.assertEqual(convert.remove_end_tags(html_string), '<html><head><title>Hello;;;')

    def test_remove_end_tags_web_page(self):

        convert = Convert()

        html_string = '<html><head><title>Hello</title></head><body><p>World</p></body></html>'

        self.assertEqual(convert.remove_end_tags(html_string), '<html><head><title>Hello;;<body><p>World;;;')

    def test_clean_start_tags(self):

        convert = Convert()

        html_string = '<title>Hello;'

        self.assertEqual(convert.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_with_head(self):

        convert = Convert()

        html_string = '<head><title>Hello;'

        self.assertEqual(convert.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_with_html(self):

        convert = Convert()

        html_string = '<html><head><title>Hello;'

        self.assertEqual(convert.clean_start_tags(html_string), '<title>Hello;')

    def test_clean_start_tags_web_page(self):

        convert = Convert()

        html_string = '<html><head><title>Hello;;<body><p>World;;;'

        self.assertEqual(convert.clean_start_tags(html_string), '<title>Hello;;<p>World;;;')

    def test_remove_hanging_colons(self):

        convert = Convert()

        colons = ';;;;'

        self.assertEqual(convert.remove_hanging_colons(colons), ';')

    def test_remove_hanging_colons_with_text(self):

        convert = Convert()

        string = ';hello;;;'

        self.assertEqual(convert.remove_hanging_colons(string), ';hello;')

    def test_remove_hanging_colons_with_html(self):

        convert = Convert()

        html_string = '<title>Hello;;<p>World;;;'

        self.assertEqual(convert.remove_hanging_colons(html_string), '<title>Hello;<p>World;')

    def test_tag_to_key(self):

        convert = Convert()

        html_string = '<title>'

        self.assertEqual(convert.tag_to_key(html_string), 'title:')

    def test_tag_to_key_tag_and_text(self):

        convert = Convert()

        html_string = '<title>Hello;<p>World;'

        self.assertEqual(convert.tag_to_key(html_string), 'title:Hello;p:World;')

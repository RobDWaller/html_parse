import unittest

class TestLinks(unittest.TestCase):

    def test_build_links(self):

        parser = Parser('<a href="https://google.com">Hello Google</a>')

        links = parser.build_links().get_links()

        self.assertEqual(links[0]['url'], 'https://google.com')
        self.assertEqual(links[0]['text'], 'Hello Google')

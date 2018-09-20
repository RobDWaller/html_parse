import unittest

class TestImages(unittest.TestCase):

    def test_build_images():

        parser = Parser('<img src="https://google.com" alt="Hello Google">')

        images = parser.build_images().get_images()

        self.assertEqual(images[0]['src'], 'https://google.com')
        self.assertEqual(images[0]['text'], 'Hello Google')

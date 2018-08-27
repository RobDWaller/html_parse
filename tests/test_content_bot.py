from content_bot import main
from content_bot.src.content import Content
import unittest

class TestContentBot(unittest.TestCase):

    def test_get(self):

        result = main.get('https://google.com')

        self.assertIsInstance(result, Content)

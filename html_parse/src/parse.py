'''
Module contains Parse class which is returned after the HTML string has been
parsed
'''
import json

class Parse:
    '''
    Parse class which is constructed after the HTML string has been parsed to
    JSON. Class also contains helper methods to access useful content.
    '''
    def __init__(self, html_data):
        self.html_data = html_data

    def get_html_data(self):
        '''
        return the html_data array
        '''
        return self.html_data

    def get_title(self):
        '''
        Get the title of the html document
        '''

        def func(html_data):
            for value in html_data:
                return 'title' in value

        result = list(filter(func, self.html_data))

        return result[0]['title']

    def get_json(self):
        '''
        Turn the the html data into a json string and return it
        '''
        return json.dumps(self.html_data)

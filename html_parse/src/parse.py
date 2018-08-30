'''
Module contains Parse class which is returned after the HTML string has been
parsed
'''
class Parse:
    '''
    Parse class which is constructed after the HTML string has been parsed to
    JSON. Class also contains helper methods to access useful content.
    '''
    def __init__(self, json):
        self.json = json

    def get_json(self):
        '''
        return the json string
        '''
        return self.json

    def get_title(self):
        '''
        Get the title of the html string
        '''
        return self.json

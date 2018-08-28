'''
Main module / interface for the HTML Parse package. One method available will
return a Parse object containing JSON object and helper methods
'''
from .src.parse import Parse

def parse(html_string):
    '''
    Parse an html string and return a Parse object containing JSON object and
    helper methods
    '''

    return Parse()

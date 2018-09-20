'''
Module to parse HTML string into a content focused JSON string. Contains class
with methods.
'''
import re

class Parser:
    '''
    Class to parse HTML string into a content focused JSON string. Follows a
    step by step pattern.
    '''

    def __init__(self, string):
        self.string = string
        self.array = []
        self.links = []

    def get_string(self):
        return self.string

    def get_array(self):
        return self.array

    def remove_attributes(self):
        self.string = re.sub('\s[a-z]*\=\".*\"', '', self.get_string())

        return self

    def remove_end_tags(self):
        '''
        Strip all HTML closing tags from html string replace with semi-colons
        '''
        self.string = re.sub('</[a-z]*>', '|;|', self.get_string())

        return self

    def clean_start_tags(self):
        '''
        Remove nested opening HTML tags from string. Will loop recursively
        until complete
        '''

        self.string = re.sub('<[a-z]*>(<[a-z]*>)', r'\g<1>', self.get_string())

        if re.match('<[a-z]*><[a-z]*>', self.get_string()):
            return self.clean_start_tags()

        return self

    def remove_hanging_colons(self):
        '''
        Remove any doubled up semi-colons from string
        '''

        self.string = re.sub('[|;|]{2,}', '|;|', self.get_string())

        return self

    def tag_to_key(self):
        '''
        Replace opening html tag in front of content with name of tag and colon
        '''
        self.string = re.sub('<([a-z]*)>', r'\g<1>|:|', self.get_string())

        return self

    def to_array(self):
        '''
        Remove ending |;| delimiter and explode processed string into array
        on |;| delimiter
        '''
        self.array = re.sub(r'\|\;\|$', '', self.get_string()).split('|;|')

        return self

    def to_dicts(self):
        '''
        Turns the array of values into an array of dicts
        '''

        array = []

        for value in self.array:
            result = value.split('|:|')

            array.append({result[0]: re.sub(r'\|$', '', result[1])})

        self.array = array

        return self

    def parse(self):
        '''
        Class interface to run all the methods in order and parse html string
        '''

        return self.remove_attributes() \
            .remove_end_tags() \
            .clean_start_tags() \
            .remove_hanging_colons() \
            .tag_to_key() \
            .to_array() \
            .to_dicts() \
            .get_array()

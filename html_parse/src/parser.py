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

    @staticmethod
    def remove_end_tags(html_string):
        '''
        Strip all HTML closing tags from html string replace with semi-colons
        '''

        return re.sub('</[a-z]*>', '|;|', html_string)

    @classmethod
    def clean_start_tags(cls, string):
        '''
        Remove nested opening HTML tags from string. Will loop recursively
        until complete
        '''

        string = re.sub('<[a-z]*>(<[a-z]*>)', r'\g<1>', string)

        if re.match('<[a-z]*><[a-z]*>', string):
            return cls.clean_start_tags(string)

        return string

    @staticmethod
    def remove_hanging_colons(string):
        '''
        Remove any doubled up semi-colons from string
        '''

        return re.sub('[|;|]{2,}', '|;|', string)

    @staticmethod
    def tag_to_key(string):
        '''
        Replace opening html tag in front of content with name of tag and colon
        '''

        return re.sub('<([a-z]*)>', r'\g<1>|:|', string)

    @staticmethod
    def to_array(string):
        '''
        Remove ending |;| delimiter and explode processed string into array
        on |;| delimiter
        '''
        return re.sub(r'\|\;\|$', '', string).split('|;|')

    @staticmethod
    def to_dicts(array):
        '''
        Turns the array of values into an array of dicts
        '''

        new_array = []

        for value in array:
            result = value.split('|:|')

            new_array.append({result[0]: re.sub(r'\|$', '', result[1])})

        return new_array

    def parse(self, html_string):
        '''
        Class interface to run all the methods in order and parse html string
        '''

        result = self.remove_end_tags(html_string)
        result = self.clean_start_tags(result)
        result = self.remove_hanging_colons(result)
        result = self.tag_to_key(result)
        result = self.to_array(result)
        return self.to_dicts(result)

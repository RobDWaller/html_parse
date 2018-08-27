import re

class Convert:

    def remove_end_tags(self, html_string):

        return re.sub('</[a-z]*>', ';', html_string)

    def clean_start_tags(self, string):

        string = re.sub('<[a-z]*>(<[a-z]*>)', '\g<1>', string)

        if re.match('<[a-z]*><[a-z]*>', string):
            return self.clean_start_tags(string)

        return string

    def remove_hanging_colons(self, string):

        return re.sub('[;]{2,}', ';', string)

    def tag_to_key(self, string):

        return re.sub('<([a-z]*)>', '\g<1>:', string)

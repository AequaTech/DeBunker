from typing import Dict
import string

class Sensationalism:

    def __init__(self,title: str = None, req_id: str = None) -> None:

        self.title = title
        self.req_id = req_id

    def upc_w_ratio(self) -> Dict[float,str]:
        """
        returns the ratio between the number of upper-cased words and
        the total number of words:
        n_upper_words / n_words
        """
        import regex as re

        assert type(self.title) == str,"I need a string to compute this metric"

        title = self.title

        up_pattern = re.compile('[A-Z]+')
        all_w_pattern = re.compile('\w+')

        n_upper_words = len(re.findall(up_pattern,title))
        n_words = len(re.findall(all_w_pattern,title))

        ratio = n_upper_words/n_words

        desc_eng = "There is at least one upper case word in the title" if ratio >0 else "There are no upper case words in the title"

        upc_ratio = {'upc_ratio':ratio,'description':desc_eng}

        return upc_ratio

    def emp_punct_ratio(self) -> Dict[int,str]:
        """
        returns the number of emphatic punctuations
        """
        import regex as re

        assert type(self.title) == str,"I need a string to compute this metric"

        title = self.title

        punct_pattern = re.compile('(\?|!)')

        punct = len(re.findall(punct_pattern,title))

        desc_eng = "There is at least one emphatic punctuation mark in the title" if punct >0 else "There are no emphatic punctuation marks in the title"

        emp_punct_ratio = {'emp_punct_ratio':punct,'description':desc_eng}

        return emp_punct_ratio

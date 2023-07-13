from typing import Dict, Union

import numpy as np
import regex as re
import emojis
import numpy
from aequaTech_packages.analysis import affective_analyses
import textstat
from random import random

class Sensationalism:

    def __init__(self) -> None:
        self.sentiment_analysis = affective_analyses.Sentix()

        self.emotion_analysis = affective_analyses.Emotions_NRC('it')

        textstat.set_lang('it')

    ############
    # informal style
    ############

    def informal_style(self,url):
        ratio_upper_case=self.__ratio_upper_case(url)
        ratio_repeated_letters=self.__ratio_repeated_letters(url)
        punct_count=self.__punct_count(url)
        check_emoji=self.__check_emoji(url)


        return {'overall': numpy.average([ratio_upper_case['overall'],ratio_repeated_letters['overall'],punct_count['overall'],check_emoji['overall']], ),
                'ratio_upper_case': ratio_upper_case,
                'ratio_vowel_repetition': ratio_repeated_letters,
                'punct_count': punct_count,
                'check_emoji': check_emoji,
        }

    def __ratio_upper_case(self, url) ->  Dict[str, Union[str, float]]:
        """
        returns the ratio between the number of upper-cased words and
        the total number of words:
        n_upper_words / n_words
        """

        #assert type(url.title) == str,"I need a string to compute this metric"

        title = url.title

        up_pattern = re.compile('[A-Z]{}')
        all_w_pattern = re.compile('\w+')

        n_upper_words = len(re.findall(up_pattern,title))
        n_words = len(re.findall(all_w_pattern,title))

        ratio = n_upper_words/n_words

        desc_eng = "There is at least one upper case word in the title" if ratio >0 else "There are no upper case words in the title"

        upc_ratio = {'overall':ratio,'description':desc_eng}

        return upc_ratio

    def __ratio_repeated_letters(self, url) ->  Dict[str, Union[str, float]]:
        """
        es. SVEGLIAAAA
        returns the ratio between the number of upper-cased words and
        the total number of words:
        n_upper_words / n_words
        """

        #assert type(url.title) == str,"I need a string to compute this metric"

        title = url.title

        up_pattern = re.compile('[A-z]{1,}([aA]{3,}|[eE]{3,}|[iI]{3,}|[oO]{3,}|[uU]{3,})')
        all_w_pattern = re.compile('\w+')

        n_upper_words = len(re.findall(up_pattern,title))
        n_words = len(re.findall(all_w_pattern,title))

        ratio = n_upper_words/n_words

        desc_eng = "There is at least one word with a repeated letter e.g. svegliaaa!" if ratio >0 else "There are no upper case words in the title"

        upc_ratio = {'overall':ratio,'description':desc_eng}

        return upc_ratio

    def __punct_count(self,url) ->  Dict[str, Union[str, float]]:
        """
        returns the number of emphatic punctuations
        """

        title = url.title

        punct_normal = re.compile('(\?|.|,|;|:)')
        punct_weird = re.compile('(\!|(...)|…|\*|=|$)')

        num_normal = len(re.findall(punct_normal,title))
        num_weird = len(re.findall(punct_weird,title))

        desc_eng_normal = "There is at least one normal punctuation mark in the title" if num_normal >0 else "There are no normal punctuation marks in the title"
        desc_eng_weird = "There is at least one weird punctuation mark in the title" if num_normal >0 else "There are no weird punctuation marks in the title"

        emp_punct_count = {'punct_num_normal':num_normal,'description_normal':desc_eng_normal,
                           'punct_num_weird':num_weird,'description_weird':desc_eng_weird,
                           'overall': 1 if num_weird > num_normal else 0, 'description': '1 if weird punctuation marks are more than normal ones'
                           }

        return emp_punct_count

    def __check_emoji(self,url) -> Dict[str, Union[str, float]]:
        new_list = emojis.get(url.title)


        check_emoji = {
                           'overall': 1 if len(new_list) > 0 else 0,
                           'description': '1 if the is at least one emoji'
                           }
        return check_emoji


    ############
    # sentiment and affective analysis
    ############
    def get_affective_analysis(self, url) -> Dict[str, Union[str, float]]:

        senitiment_profile = self.sentiment_analysis.sentiment_by_sent(url.title)
        emotion_profile = self.emotion_analysis.emotions_by_sent(url.title)
        senitiment_profile['overall']=senitiment_profile['polarity']
        emotion_profile['overall']=np.average([value for value in emotion_profile.values()])
        return {
            'overall' : np.average([  senitiment_profile['overall'],  emotion_profile['overall']]),
            'senitiment_profile' : senitiment_profile,
            'emotion_profile' : emotion_profile

        }


    ############
    # readability, complexity, and grade level
    ############
    def get_readability_scores(self, url) -> Dict[str, Union[str, float]]:

        flesch_reading_ease = textstat.flesch_reading_ease(url.title)
        #the maximum score is 121.22, there is no limit on how low the score can be. A negative score is valid.
        #90-100	Very Easy
        #60-69	Standard
        #0-29	Very Confusing
        flesch_reading_ease = flesch_reading_ease / 100
        flesch_reading_ease = abs(0.65 - flesch_reading_ease) * 2
        if flesch_reading_ease > 1:
            flesch_reading_ease = 1

        gunning_fog = textstat.gunning_fog(url.title)
        #17	College graduate
        #12	High school senior
        #6	Sixth grade
        gunning_fog = (gunning_fog - 6) / (17 - 6)

        return {
            'overall' : np.average([flesch_reading_ease,gunning_fog]),
            'flesch_reading_ease' : flesch_reading_ease,
            'gunning_fog' : gunning_fog,

        }

    ############
    # colloquial style
    ############
    def get_clickbait_style(self, url) -> Dict[str, Union[str, float]]:


        return {
            'overall': random(),
            'personal_score': random(),
            'intensifier_score': random(),
            'modal_scoree': random(),
            'numeral_score': random(),
            'shortened_form_score': random(),
            'interrogative_score': random(),
        }



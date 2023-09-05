from typing import Dict, Union

import numpy as np
import regex as re
import emojis
import numpy
from aequaTech_packages.analysis import affective_analyses
import textstat
from random import random
import spacy
import sys

class Sensationalism:

    def __init__(self) -> None:
        self.sentiment_analysis = affective_analyses.Sentix()

        self.emotion_analysis = affective_analyses.Emotions_NRC('it')
        textstat.set_lang('it')
        self.nlp = spacy.load("it_core_news_lg")

    ############
    # informal style
    ############

    def informal_style(self,url):
        ratio_upper_case=self.__ratio_upper_case(url)
        ratio_repeated_letters=self.__ratio_repeated_letters(url)
        punct_count=self.__punct_count(url)
        check_emoji=self.__check_emoji(url)

        print({'overall': numpy.average([ratio_upper_case['overall'],ratio_repeated_letters['overall'],punct_count['overall'],check_emoji['overall']], ),
                'ratio_upper_case': ratio_upper_case,
                'ratio_vowel_repetition': ratio_repeated_letters,
                'punct_count': punct_count,
                'check_emoji': check_emoji,
        })
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

        ratio = n_upper_words/n_words if n_words > 0 else 0

        desc_eng = "There is at least one upper case word in the title" if ratio >0 else "There are no upper case words in the title"

        upc_ratio = {'overall':ratio,'description':desc_eng}
        print({'overall':ratio,'description':desc_eng})

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

        ratio = n_upper_words/n_words if n_words>0 else 0

        desc_eng = "There is at least one word with a repeated letter e.g. svegliaaa!" if ratio >0 else "There are no upper case words in the title"

        upc_ratio = {'overall':ratio,'description':desc_eng}
        print({'overall':ratio,'description':desc_eng})

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
        print({'punct_num_normal':num_normal,'description_normal':desc_eng_normal,
                           'punct_num_weird':num_weird,'description_weird':desc_eng_weird,
                           'overall': 1 if num_weird > num_normal else 0, 'description': '1 if weird punctuation marks are more than normal ones'
                           })

        return emp_punct_count

    def __check_emoji(self,url) -> Dict[str, Union[str, float]]:
        new_list = emojis.get(url.title)

        print({
                           'overall': 1 if len(new_list) > 0 else 0,
                           'description': '1 if the is at least one emoji'
                           })
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
        print({
            'overall' : np.average([  senitiment_profile['overall'],  emotion_profile['overall']]),
            'senitiment_profile' : senitiment_profile,
            'emotion_profile' : emotion_profile

        })
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

        #gunning_fog = textstat.gunning_fog(url.title)
        #17	College graduate
        #12	High school senior
        #6	Sixth grade
        #gunning_fog = (gunning_fog - 6) / (17 - 6)
        print({
            'overall' : np.average([flesch_reading_ease]),#,gunning_fog]),
            'flesch_reading_ease' : flesch_reading_ease,
            #'gunning_fog' : gunning_fog,

        })
        return {
            'overall' : np.average([flesch_reading_ease]),#,gunning_fog]),
            'flesch_reading_ease' : flesch_reading_ease,
            #'gunning_fog' : gunning_fog,

        }

    ############
    # colloquial style
    ############
    def get_clickbait_style(self, url) -> Dict[str, Union[str, float]]:

        linguistic_fetures=self.nlp(url.title)
        print(type(linguistic_fetures))
        personals=0
        personals_and_impersonals=0 #avoid division by 0

        adj=0
        adj_intensified=0 #avoid division by 0

        modals=0
        modals_and_not=0 #avoid division by 0

        numeral=0
        numeral_and_not=0 #avoid division by 0

        senteces_interrogative=0
        senteces=0 #avoid division by 0

        for sent in linguistic_fetures.sents:
            senteces+=1
            if '?' in sent.text:
                senteces_interrogative+=1

            for token in sent:
                if 'Persons' in token.morph.to_dict():
                    personals_and_impersonals += 1
                    if token.morph.to_dict()['Person'] == '1' or token.morph.to_dict()['Person'] == '2':
                        personals += 1

                #intensifier_score
                if token.pos_=='ADJ':
                    adj+=1
                    if 'Degree' in token.morph.to_dict(): #@cignarella, piccolissimo non ha degree, non viene contato come intesifier piccolissimo ADJ A amod adjective None Gender=Masc|Number=Sing {'Gender': 'Masc', 'Number': 'Sing'}
                        adj_intensified += 1


                #@cignarella, modal score. I modali esistono solo per adj e noun?
                #cosa è indicativo della presenza di sensazionalismo? Molti modal o pochi?
                if token.pos_=='ADJ' or token.pos_=='NOUN':
                    modals_and_not+=1
                    if 'mod' in token.dep_:
                        modals += 1

                #@cignarella, cosa è indicativo della presenza di sensazionalismo? molti numeri o pochi numeri?
                if token.pos_ == 'NUM':
                    numeral_and_not+=1
                    if 'mod' in token.dep_:
                        numeral+=1

        personal_score= personals/personals_and_impersonals if personals_and_impersonals>0 else 0
        intensifier_score=adj_intensified/adj if adj>0 else 0
        modal_score=modals/modals_and_not if modals_and_not>0 else 0
        numeral_score=modals/numeral_and_not if numeral_and_not>0 else 0
        interrogative_score=senteces_interrogative/senteces if senteces>0 else 0
        shortened_form_score=random()
        print({
            'overall': numpy.average([personal_score,intensifier_score,modal_score,numeral_score,shortened_form_score,interrogative_score]),
            'personal_score': personal_score,
            'intensifier_score': intensifier_score,
            'modal_scoree': modal_score,
            'numeral_score': numeral_score,
            'shortened_form_score': shortened_form_score, #@cignarella, come trovo le interrogative?
            'interrogative_score': interrogative_score,
        })
        return {
            'overall': float(numpy.average([personal_score,intensifier_score,modal_score,numeral_score,shortened_form_score,interrogative_score])),
            'personal_score': personal_score,
            'intensifier_score': intensifier_score,
            'modal_scoree': modal_score,
            'numeral_score': numeral_score,
            'shortened_form_score': shortened_form_score, #@cignarella, come trovo le interrogative?
            'interrogative_score': interrogative_score,
        }


if __name__ == '__main__':
    sensationalism = Sensationalism()

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


        return {'overall': numpy.max([ratio_upper_case['overall'],ratio_repeated_letters['overall'],punct_count['overall'],check_emoji['overall']], ),
                'ratio_upper_case': ratio_upper_case,
                'ratio_vowel_repetition': ratio_repeated_letters,
                'punct_count': punct_count,
                'check_emoji': check_emoji,
                'description': "overall report the max value among the single informal style features"
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
        #print({'overall':ratio,'description':desc_eng})

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

        up_pattern = re.compile('[A-z]{1,}([aA]{2,}|[eE]{2,}|[iI]{2,}|[oO]{2,}|[uU]{2,})')
        all_w_pattern = re.compile('\w+')

        n_upper_words = len(re.findall(up_pattern,title))
        n_words = len(re.findall(all_w_pattern,title))

        ratio = n_upper_words/n_words if n_words>0 else 0

        desc_eng = "There is at least one word with a repeated letter e.g. svegliaaa!" if ratio >0 else "There are no words with a repeated letter e.g. svegliaaa!"

        upc_ratio = {'overall':ratio,'description':desc_eng}
        #print({'overall':ratio,'description':desc_eng})

        return upc_ratio

    def __punct_count(self,url) ->  Dict[str, Union[str, float]]:
        """
        returns the number of emphatic punctuations
        """

        title = url.title

        punct_normal = re.compile('(\?|\.|\,|\;|\:)')
        punct_weird = re.compile('(\!|(\.\.\.)|…|\*|\=|\$)')

        num_normal = len(re.findall(punct_normal,title))
        num_weird = len(re.findall(punct_weird,title))

        desc_eng_normal = "There is at least one normal punctuation mark in the title" if num_normal >0 else "There are no normal punctuation marks in the title"
        desc_eng_weird = "There is at least one weird punctuation mark in the title" if num_normal >0 else "There are no weird punctuation marks in the title"

        emp_punct_count = {'punct_num_normal':num_normal,'description_normal':desc_eng_normal,
                           'punct_num_weird':num_weird,'description_weird':desc_eng_weird,
                           'overall': num_weird/(num_weird+num_normal) if num_weird+num_normal > 0 else 0, 'description': 'ratio between weird punctuation marks and the total number of punctuaction marks'
                           }


        return emp_punct_count

    def __check_emoji(self,url) -> Dict[str, Union[str, float]]:
        new_list = emojis.get(url.title)


        check_emoji = {
                           'overall': len(new_list)/len(url.title.split()) if len(url.title.split()) > 0 else 0,
                           'description': 'ratio of emojis in the text and tokens'
                           }
        return check_emoji


    ############
    # sentiment and affective analysis
    ############
    def get_affective_analysis(self, url) -> Dict[str, Union[str, float]]:

        sentiment_profile = self.sentiment_analysis.sentiment_by_sent(url.title)
        emotion_profile = self.emotion_analysis.emotions_by_sent(url.title)
        sentiment_profile['overall']=abs(sentiment_profile['polarity'])
        emotion_profile['overall']=np.average([value for value in emotion_profile.values()])

        return {
            'overall' : np.median([  round(sentiment_profile['overall'],3),  round(emotion_profile['overall'],3)]),
            'sentiment_profile' : sentiment_profile,
            'emotion_profile' : emotion_profile,
            'description' : "the max value between emotion and sentiment profiles"
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
        count_token = 0

        personals=0

        adj=0
        adj_intensified=0 #avoid division by 0

        modals=0
        modals_and_not=0 #avoid division by 0

        numeral=0

        senteces_interrogative=0
        senteces=0 #avoid division by 0
        shortened_form=0

        for sent in linguistic_fetures.sents:

            # interrogative_score
            senteces+=1
            if '?' in sent.text:
                senteces_interrogative+=1

            for token in sent:

                count_token+=1

                # personal score
                personali_soggetto=['io', 'tu', 'egli', 'ella', 'noi', 'voi', 'essi', 'lui', 'lei', 'loro', 'esso', 'essa', 'esse']
                personali_complemento=['me', 'mi', 'te', 'ti', 'lui', 'sé', 'ciò', 'lei', 'lo', 'gli', 'ne', 'si', 'la', 'le', 'noi', 'ci', 'voi', 'vi', 'essi', 'loro', 'esse', 'li', 'le']
                pronomi_dimostrativi=['questo','codesto','quello','questa','codesta','quella','questi','codesti','quelli','queste','codeste','quelle','stesso','stessa','stessi','stesse',
                                      'medesimo','medesima','medesime','medesimi','tale','tali','costui','costei','costoro','colui','colei','coloro','ciò']
                if token.text.lower() in personali_soggetto+personali_complemento+pronomi_dimostrativi:
                    personals += 1

                #intensifier_score
                if token.pos_=='ADJ':
                    adj+=1
                    if 'Degree' in token.morph.to_dict() and (token.morph.to_dict()['Degree']=='Sup' or token.morph.to_dict()['Degree']=='Abs' ):
                        adj_intensified += 1


                #modal_scoree
                if token.pos_=='VERB':
                    modals_and_not+=1
                    if token.lemma_ in ['potere','volere','dovere']:
                        modals += 1

                # numeral_score
                if token.pos_ == 'NUM':
                    numeral+=1

                # shortened_form_score
                if token.text.lower() in ['xke', 'xké', 'tadb', 'tat', 'k', 'kk', 'tl;dr', 'thx', 'tvtb', 'tvukdb', 'xoxo', 'tbh', 'scnr', 'rly?', 'rofl', 'plz', 'omg', 'omfg', 'nsfw', 'n8', 'n1', 'noob', 'n00b', 'lol', 'irl', 'imho', 'imo', 'idk', 'Hth', 'Hf', 'gratz', 'gg', 'gl', 'gj', 'gn', 'g2g', 'gig', 'fyi', 'faq', 'f2f', 'eod', 'ez', 'dafuq', 'dafuq', 'wtf', 'cya', 'cbcr', 'btw', 'brb', 'bbl', 'bg', 'asap', 'afaik', 'aka', '2L8', '2g4u', 'ime', 'b4', 'rsvp', 'lmk', 'dob', 'eta', 'fomo', 'diy', 'fwiw', 'hmu', 'icymi', 'tbh', 'tbf']:
                    shortened_form += 1


        personal_score= personals/count_token if count_token>0 else 0
        intensifier_score=adj_intensified/adj if adj>0 else 0
        modal_score=modals/modals_and_not if modals_and_not>0 else 0
        numeral_score=modals/count_token if count_token>0 else 0
        interrogative_score=senteces_interrogative/senteces if senteces>0 else 0
        shortened_form_score=shortened_form/count_token if count_token>0 else 0

        return {
            'overall': float(numpy.median([round(personal_score,3),round(intensifier_score,3),round(modal_score,3),round(numeral_score,3),round(shortened_form_score,3),round(interrogative_score,3)])),
            'personal_score': personal_score,
            'intensifier_score': intensifier_score,
            'modal_score': modal_score,
            'numeral_score': numeral_score,
            'shortened_form_score': shortened_form_score,
            'interrogative_score': interrogative_score,
            'description': 'median value among clickbait features'
        }


if __name__ == '__main__':
    sensationalism = Sensationalism()



    text='cmq '

    print(sensationalism.get_clickbait_style(text))



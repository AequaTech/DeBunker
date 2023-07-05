import re,spacy
from transformers import AutoTokenizer
import torch
import io

class PreprocessingSpacy:

    languages = { 'it' : "it_core_news_lg", 'en': "en_core_web_lg"}

    def __init__(self, language):

        """Load given model."""
        if language == "it":
            self.nlp=spacy.load(self.languages["it"])
            self.stopwords=self.list_stopwords(path_stopwords)
        elif language == "en":
            self.nlp=spacy.load(self.languages["en"])
            self.stopwords= self.nlp.Defaults.stop_words
        else:
            raise Exception("Language not supported")

        self.language = language

    def list_stopwords(self, path):
        with open(path, 'r', encoding='utf8') as f:
            r=f.read()
            sw=r.split('\n')
        return sw

    def cleaning(self, text):
        string = text.lower()
        string = re.sub(r"((http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?)", " ", string, flags=re.U)
        # string = re.sub(r'[@#]', ' ', string, flags=re.U)
        string = re.sub(r"([\.\,\!\?\;\:\-\_\|“”\"\'\\\/\%\&\$\£\€\@\#\[\]\)\(])", r" \1 ", string)
        string = re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", string)
        string = re.sub(r"[^a-zA-Z0-9àèéìùòç]",r" ", string)
        string = re.sub(r"\s+",r" ", string)
        return string.strip()

    def preprocess_sent(self,text):
        output_dict = dict()

        text_cleaned= self.cleaning(text)

        tokenized = self.nlp(text_cleaned)
        lemmatized = ' '.join([i.lemma_ for i in tokenized])
        pos = ' '.join([i.label_ for i in tokenized])
        tokenized = ' '.join([i.text for i in tokenized])

        output_dict['lemmatized'] = lemmatized
        output_dict['pos'] = pos
        output_dict['tokenized'] = tokenized

        return output_dict

class BertBasedTokenizer:
    def __init__(self,model):
        self.model = model

    def tokenize_text(self,text):

        model = self.model
        tokenizer = AutoTokenizer.from_pretrained(model)
        tokenized = tokenizer.encode_plus(text,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']
        buffer = io.BytesIO()
        torch.save(feat, buffer)
        feat = buffer.getvalue()
        buffer = io.BytesIO()
        torch.save(attention, buffer)
        attention = buffer.getvalue()
        return feat,attention





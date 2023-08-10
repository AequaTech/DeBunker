import re,spacy
from transformers import AutoTokenizer
import torch
import io
#from scispacy.abbreviation import AbbreviationDetector
from spacy.tokens import DocBin

class PreprocessingSpacy:

    languages = { 'it' : "it_core_news_lg", 'en': "en_core_web_lg"}

    def __init__(self, language):

        """Load given model."""
        if language == "it":
            self.nlp=spacy.load(self.languages["it"])
        elif language == "en":
            self.nlp=spacy.load(self.languages["en"])
        else:
            raise Exception("Language not supported")


        #abbreviation_pipe = AbbreviationDetector(self.nlp)
        #self.nlp.add_pipe(abbreviation_pipe)
        self.language = language


    def get_linguistic_features_from_text(self,text):
        doc_bin = DocBin(attrs=["LEMMA", "ENT_IOB", "ENT_TYPE"], store_user_data=True)
        doc_bin.add(self.nlp(text))
        bytes_data = doc_bin.to_bytes()
        return bytes_data

    def get_linguistic_features_from_bytes(self, bytes_data):
        nlp = spacy.blank("it_core_news_lg")
        doc_bin = DocBin().from_bytes(bytes_data)
        docs = list(doc_bin.get_docs(nlp.vocab))
        return docs[0]

class BertBasedTokenizer:
    def __init__(self,model):
        self.model = model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model)


    def tokenize_text(self,text):

        tokenized = self.tokenizer.encode_plus(text,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']
        buffer = io.BytesIO()
        torch.save(feat, buffer)
        feat = buffer.getvalue()
        buffer = io.BytesIO()
        torch.save(attention, buffer)
        attention = buffer.getvalue()
        return feat,attention





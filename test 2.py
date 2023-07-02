from transformers import AutoTokenizer
import torch
import io
import numpy as np

class BertBasedTokenizer:
    def __init__(self,model):
        self.model = model

    def tokenize_text(self,text):

        model = self.model
        tokenizer = AutoTokenizer.from_pretrained(model)
        tokenized = tokenizer.encode_plus(text,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']

        return feat,attention


s = 'i musulmani ammazzano tutti quelli che per il loro fumoso cervello sono " infedeli " . i nostri terroristi istituzionali ci obbligano ad accogliere e mantenere i nostri assassini'
tokenizer = BertBasedTokenizer('dbmdz/bert-base-italian-cased')
feat, attention = tokenizer.tokenize_text(s)

print(feat)
buffer = io.BytesIO()
torch.save(feat, buffer)
binary=buffer.getvalue()
print(binary)
frameTensor = torch.load(io.BytesIO(binary))
print(frameTensor)
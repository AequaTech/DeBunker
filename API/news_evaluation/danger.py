from transformers import AutoConfig,AutoModel,AutoTokenizer
import torch.nn as nn
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification




class Danger():

    def __init__(self,model_name: str = None, num_classes: int = None,stereo_cp=None,irony_cp=None,fake_cp=None,flame_cp=None):
        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=2)




    def stereotype_detection(self,title: str = None):#, req_id: str = None): si occupa fastapi del caching
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        tokenized = tokenizer.encode_plus(title,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']

        model = self.model

        #model.load_state_dict(torch.load('state_dict.pth'))

        model.eval()

        result = model(input_ids=feat,attention_mask=attention)

        return torch.argmax(result['logits'].detach()).item()


def main():
    model = Danger('distilbert-base-uncased',2)
    req = 123
    s = 'I hate immigrants!'
    res = model.stereotype_detection(title=s) #,req_id=req)si occupa fastapi del caching
    #print(torch.argmax(res['logits']).item())
    return torch.argmax(res['logits']).item()

if __name__=='__main__':

    main()

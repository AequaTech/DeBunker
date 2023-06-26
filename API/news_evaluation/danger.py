from transformers import AutoConfig,AutoModel,AutoTokenizer
import torch.nn as nn
import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from safetensors.torch import load_model, load_file

class Danger():

    def __init__(self,model_name: str = None, num_classes: int = None, task='flame'):
                 # stereo_cp=None,irony_cp=None,fake_cp=None,flame_cp=None):
        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=num_classes)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        
        if task == 'stereo':
            self.cp = '\DeBunker\API\resources\models\stereo.safetensors' 
        elif task == 'flame':
            self.cp = r"\DeBunker\API\resources\models\hs.safetensors"
        elif task == 'iro':
            self.cp = '\DeBunker\API\resources\models\iro.safetensors' 
        else:
            self.cp = '\DeBunker\API\resources\models\sarcasm.safetensors' #sarcasm


    def classification(self,title: str = None):#, req_id: str = None): si occupa fastapi del caching
        tokenized = self.tokenizer.encode_plus(title,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']

        model = self.model

        model.load_state_dict(load_file(self.cp))

        model.eval()

        result = model(input_ids=feat,attention_mask=attention)
        # print(torch.argmax(result['logits'].detach()).item(), '\t', result)

        return torch.argmax(result['logits'].detach()).item()


def main():
    # model = Danger('distilbert-base-uncased',2)
    model = Danger('dbmdz/bert-base-italian-cased', 2, task='flame')
    req = 123
    # s = 'I hate immigrants!'
    s = 'i musulmano ammazzano tutti quelli che per il loro fumoso cervello sono " infedeli " . i nostri terroristi istituzionali ci obbligano ad accogliere e mantenere i nostri assassini'
    res = model.classification(title=s) #,req_id=req)si occupa fastapi del caching
    #print(torch.argmax(res['logits']).item())
    return res

if __name__=='__main__':

    main()

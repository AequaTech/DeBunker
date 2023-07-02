from transformers import AutoConfig,AutoModel,AutoTokenizer
import torch.nn as nn
import torch,sys
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from safetensors.torch import load_model, load_file
sys.path.insert(1,'../webScraper/')

from WebScraper import BertBasedTokenizer

class Danger():

    def __init__(self,model_name: str = None, num_classes: int = None,cp: str = None, task='flame'):
                 # stereo_cp=None,irony_cp=None,fake_cp=None,flame_cp=None):
        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=num_classes)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.cp = cp
        '''
        if task == 'stereo':
            self.cp = '\DeBunker\API\resources\models\stereo.safetensors'
        elif task == 'flame':
            self.cp = r"\DeBunker\API\resources\models\hs.safetensors"
        elif task == 'iro':
            self.cp = '\DeBunker\API\resources\models\iro.safetensors'
        else:
            self.cp = '\DeBunker\API\resources\models\sarcasm.safetensors' #sarcasm
        '''

    def classification(self,feat,attention):

        model = self.model
        cp = self.cp
        if cp is not None:
            model.load_state_dict(load_file(self.cp))
        else:
            model

        model.eval()

        result = model(input_ids=feat,attention_mask=attention)
        # print(torch.argmax(result['logits'].detach()).item(), '\t', result)

        return torch.argmax(result['logits'].detach()).item()


def main():
    # model = Danger('distilbert-base-uncased',2)
    model = Danger('dbmdz/bert-base-italian-cased', 2, task='flame')
    req = 123
    # s = 'I hate immigrants!'
    s = 'i musulmani ammazzano tutti quelli che per il loro fumoso cervello sono " infedeli " . i nostri terroristi istituzionali ci obbligano ad accogliere e mantenere i nostri assassini'
    tokenizer = BertBasedTokenizer('dbmdz/bert-base-italian-cased')
    feat,attention = tokenizer.tokenize_text(s)
    res = model.classification(feat,attention) #,req_id=req)si occupa fastapi del caching
    #print(torch.argmax(res['logits']).item())
    print(res)
    return res

if __name__=='__main__':

    main()

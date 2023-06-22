from transformers import AutoConfig,AutoModel,AutoTokenizer
import torch.nn as nn
import dlmodel.predictors as predictors
from transformers import AutoTokenizer




class Danger():

    def __init__(self,model_name: str = None, num_classes: int = None,stereo_cp=None,irony_cp=None,fake_cp=None,flame_cp=None):
        self.model_name = model_name

        self.model = predictors.BertBasedPrediction(model_name, num_classes)
        


    def stereotype_detection(self,title: str = None, req_id: str = None):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        tokenized = tokenizer.encode_plus(title,req_id,return_tensors='pt')

        feat = tokenized['input_ids']
        attention = tokenized['attention_mask']
        
        model = self.model

        model.load_state_dict(torch.load('state_dict.pth'))

        model.eval()

        result = model(features=feat,attention_mask=attention)

        return result

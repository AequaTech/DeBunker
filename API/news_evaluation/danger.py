from transformers import AutoConfig,AutoModel
import torch.nn as nn
import torch,sys
from transformers import AutoModelForSequenceClassification
from safetensors.torch import load_model, load_file
import io
import loralib
import perf
from peft import LoraConfig, get_peft_model
from peft import set_peft_model_state_dict

class Danger():

    def __init__(self,model_name: str = None, num_classes: int = None,cp: str = None, ):
                 
        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=num_classes)
        
        
    def model_lora(self, model):

        config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["query", "value"], 
        lora_dropout=0.01,
        bias="none",
        task_type="classifier",
        modules_to_save=["classifier"]
        )

        lora_model = get_peft_model(self.model, config)
        return lora_model

    def classification(self,feat,attention, task='flame'):
        """
    
        BytesIO representation of feat and attention

        """
        if task == 'stereo':
            cp = '\DeBunker\API\resources\models\stereo.safetensors'
        elif task == 'flame':
            cp = r"\DeBunker\API\resources\models\hs.safetensors"
        elif task == 'iro':
            cp = '\DeBunker\API\resources\models\iro.safetensors'
        else:
            cp = '\DeBunker\API\resources\models\sarcasm.safetensors' 

        model = model_lora(self.model)
        
        if cp is not None:
            full_state_dict =load_file(cp)
            set_peft_model_state_dict(model, full_state_dict)   
        #else:
        #    model

        model.eval()
        feat=torch.load(io.BytesIO(feat))
        attention=torch.load(io.BytesIO(attention))

        result = model(input_ids=feat,attention_mask=attention)

        return torch.argmax(result['logits'].detach()).item()
    
    def prediction(self, url):
        res = {
            'stereotype': classification(url.feat_title, url.attention_title, task='stereo'),
            'flame':classification(url.feat_title, url.attention_title, task='flame'),
            'irony': classification(url.feat_title, url.attention_title, task='iro'),
            'sarcasm': classification(url.feat_title, url.attention_title, task='sarc')
              }

if __name__=='__main__':
    ...

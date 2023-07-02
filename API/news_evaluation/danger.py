from transformers import AutoConfig,AutoModel,AutoTokenizer
import torch.nn as nn
import torch,sys
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from safetensors.torch import load_model, load_file
import io

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
        """
        @marco: classification di che? stereotipe?

        BytesIO representation of feat and attention

        """

        model = self.model
        cp = self.cp
        if cp is not None:
            model.load_state_dict(load_file(self.cp))
        #else:
        #    model

        model.eval()
        feat=torch.load(io.BytesIO(feat))
        attention=torch.load(io.BytesIO(attention))

        result = model(input_ids=feat,attention_mask=attention)

        return torch.argmax(result['logits'].detach()).item()




if __name__=='__main__':
    ...

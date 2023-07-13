from transformers import  AutoTokenizer
import torch
from transformers import AutoModelForSequenceClassification
from safetensors.torch import  load_file
import io
from peft import LoraConfig, get_peft_model
from peft import set_peft_model_state_dict
import numpy as np

class Danger():
    """Class that implements the danger dimension that consist in detecting stereotype, flame, irony, and sarcasm.
    @simona spieghi meglio cosa viene utilizzata per fare la prediction?
    """
    def __init__(self, model_name: str = None, num_classes: int = None):
        """
            input
                model_name: str es. 'dbmdz/bert-base-italian-cased'
                num_classes: int es. 2
        """
        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=num_classes)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.lora_model = self.__model_lora()


    def __model_lora(self):
        """
            @simona scrivi qui una descrizione di questo metodo? Io non so che fa
        """
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

    def __classification(self, url, task):
        """
            input
                url: object of class Urls(Base):
                task: str admitted values 'stereotype', 'flame', 'irony', and 'sarcasm'
            output:
                float between 0 and 1, result of the prediction of the task
        """
        #carico i pesi per il task specifico
        cp = 'news_evaluation/models/'+task+'.safetensors'
        full_state_dict = load_file(cp)

        #adatta il modello generale con i pesi del task specifico
        set_peft_model_state_dict(self.lora_model, full_state_dict)
        self.lora_model.eval()

        #carica il tensore a partire  dalla sua rappresentazione binaria contenuta nel database
        feat=torch.load(io.BytesIO(url.feat_title))
        attention=torch.load(io.BytesIO(url.attention_title))
        result = self.lora_model(input_ids=feat, attention_mask=attention)

        return torch.argmax(result['logits'].detach()).item()

    def prediction(self, url):
        """

            input
                url: object of class Urls(Base):
            output:
                dictionary of the prediction in the form
                {'stereotype': 1, 'flame': 1, 'irony': 0, 'sarcasm': 1, 'overall': 0.75}

        """
        res = {
                 'stereotype': self.__classification(url, task='stereotype'),
                 'flame'     : self.__classification(url, task='flame'),
                 'irony'     : self.__classification(url, task='irony'),
                 'sarcasm'   : self.__classification(url, task='sarcasm')
              }
        res['overall'] = np.average([ x for x in res.values()])

        return res


if __name__ == '__main__':
    ...
from transformers import AutoConfig, AutoModel, AutoTokenizer
import torch.nn as nn
import torch, sys
from transformers import AutoModelForSequenceClassification
from safetensors.torch import load_model, load_file
import io
import loralib
import peft  # corretto
from peft import LoraConfig, get_peft_model
from peft import set_peft_model_state_dict


class Danger():

    def __init__(self, model_name: str = None, num_classes: int = None, cp: str = None, ):

        self.model_name = model_name

        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=num_classes)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)  # usato per questa prova

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

    def classification(self, url, task='flame'):  # usato per questa prova
        # def classification(self,feat,attention, task='flame'):
        """

        BytesIO representation of feat and attention

        """
        if task == 'stereo':
            cp = 'models/stereo.safetensors'
        elif task == 'flame':
            cp = 'models/hs.safetensors'
        elif task == 'iro':
            cp = 'models/iro.safetensors'
        else:
            cp = 'models/sarcasm.safetensors'

        model = self.model_lora(self.model)

        if cp is not None:
            full_state_dict = load_file(cp)
            set_peft_model_state_dict(model, full_state_dict)
        else:
            print("models doesn't exist")

        model.eval()

        # feat=torch.load(io.BytesIO(feat))
        # attention=torch.load(io.BytesIO(attention))

        # usato per questa prova
        #tokenized = self.tokenizer.encode_plus(url., return_tensors='pt')

        #feat = tokenized['input_ids']
        #attention = tokenized['attention_mask']

        result = model(input_ids=torch.load(io.BytesIO(url.feat_title)), attention_mask=torch.load(io.BytesIO(url.attention_title)))

        return torch.argmax(result['logits'].detach()).item()

    def prediction(self, url):
        # res = {
        # 'stereotype': classification(url.feat_title, url.attention_title, task='stereo'),
        # 'flame':classification(url.feat_title, url.attention_title, task='flame'),
        # 'irony': classification(url.feat_title, url.attention_title, task='iro'),
        # 'sarcasm': classification(url.feat_title, url.attention_title, task='sarc')
        # }
        res = self.classification(url, task='flame')
        return res  # aggiunto


def main():
    #     s = 'i musulmani ammazzano tutti quelli che per il loro fumoso cervello sono " infedeli " . i nostri terroristi istituzionali ci obbligano ad accogliere e mantenere i nostri assassini'
    # tokenizer = BertBasedTokenizer('dbmdz/bert-base-italian-cased')
    # feat, attention = tokenizer.tokenize_text(s)

    # print(feat)
    # buffer = io.BytesIO()
    # torch.save(feat, buffer)
    # binary=buffer.getvalue()
    # print(binary)
    # frameTensor = torch.load(io.BytesIO(binary))
    # print(frameTensor)

    model = Danger('dbmdz/bert-base-italian-cased', 2)
    req = 123
    # s = 'I hate immigrants!'
    s = 'i musulmano ammazzano tutti quelli che per il loro fumoso cervello sono " infedeli " . i nostri terroristi istituzionali ci obbligano ad accogliere e mantenere i nostri assassini'
    res = model.prediction(s)
    print(res)


if __name__ == '__main__':
    main()
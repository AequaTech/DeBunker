from transformers import  AutoTokenizer
import torch
from transformers import AutoModelForSequenceClassification
from safetensors.torch import  load_file
import io
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

    def classification(self, url, task):  # usato per questa prova
        # def classification(self,feat,attention, task='flame'):
        """

        BytesIO representation of feat and attention

        """
        if task == 'stereo':
            cp = 'models/stereo.safetensors'
        elif task == 'flame':
            cp = 'models/hs.safetensors'
        elif task == 'iro':
            cp = 'models/irony.safetensors'
        else:
            cp = 'models/sarcasm.safetensors'

        model = self.model_lora(self.model)

        if cp is not None:
            full_state_dict = load_file(cp)
            set_peft_model_state_dict(model, full_state_dict)
        else:
            print("models doesn't exist")

        model.eval()

        result = model(input_ids=torch.load(io.BytesIO(url.feat_title)), attention_mask=torch.load(io.BytesIO(url.attention_title)))

        return torch.argmax(result['logits'].detach()).item()

    def prediction(self, url):
        res = {
         'stereotype': self.classification(url, task='stereo'),
         'flame':      self.classification(url, task='flame'),
         'irony':      self.classification(url, task='iro'),
         'sarcasm':    self.classification(url, task='sarc')
         }
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
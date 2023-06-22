import torch.nn as nn
import torch
from transformers import AutoConfig,AutoModel,AutoTokenizer
from typing import Tuple,Optional
from torch.nn import CrossEntropyLoss


class BertBasedPrediction(nn.Module):

    def __init__(self, pretrained_model_name: str, num_classes: int = None, dropout: float = 0.3):
        super().__init__()

        config = AutoConfig.from_pretrained(pretrained_model_name, num_labels=num_classes)

        self.model = AutoModel.from_pretrained(pretrained_model_name, config=config)
        self.classifier = nn.Linear(config.hidden_size, num_classes)
        self.dropout = nn.Dropout(dropout)
        self.num_labels = config.num_labels



    def forward(self, features,labels=None,attention_mask=None, head_mask=None):
        """Compute class probabilities for the input sequence.
        Args:
            features (torch.Tensor): ids of each token,
                size ([bs, seq_length]
            attention_mask (torch.Tensor): binary tensor, used to select
                tokens which are used to compute attention scores
                in the self-attention heads, size [bs, seq_length]
            head_mask (torch.Tensor): 1.0 in head_mask indicates that
                we keep the head, size: [num_heads]
                or [num_hidden_layers x num_heads]
        Returns:
            PyTorch Tensor with predicted class scores
        """
        assert attention_mask is not None, "attention mask is none"

        bert_output = self.model(features=features, attention_mask=attention_mask, head_mask=head_mask)

        seq_output = bert_output[0]
        pooled_output = seq_output.mean(axis=1)
        logits = self.classifier(pooled_output)
        score = logits.argmax()




        return logits,score

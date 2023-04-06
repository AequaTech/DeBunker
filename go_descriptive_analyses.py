import sys
sys.path.append('./aequaTech_packages/') 
from dataset import preprocess_dataset
from analysis import affective_analyses
from text import preprocess
from inference import HS_Sarcasm_Inference as hs_sarc

from nltk.tokenize import sent_tokenize,RegexpTokenizer
import yaml
import pandas as pd
import time
with open(sys.argv[1], encoding='utf8') as f:
    params = yaml.load(f, Loader=yaml.FullLoader)

def descriptive_analyses(sents):    
    list_dicts = []
    for sent in sents:
        # print('--', sent)
        
        try:
            d = dict()
            d['date'] = sent['date']
            d['doc_id'] = sent['doc_id']
            d['sent_id'] = sent['id']
            d['text'] = sent['text']
            d['sent'] = sent['sent']
            lemmatized_sent = preprocess.preprocess_sent(sent)['lemmatized']
            if not d['sent']:
                continue
            
            # print('sentiment')
            d['positive'] = sentiment_analysis.sentiment_by_sent(lemmatized_sent)['positive']
            d['negative'] = sentiment_analysis.sentiment_by_sent(lemmatized_sent)['negative']
            
            # print('emotions')
            d_emo = emotion_analysis.emotions_by_sent(lemmatized_sent)
            for k, v in d_emo.items():
                    d[k] = v

            # print('hs, sarc')
            hs, sarc, logit1, logit2 = inference_hs_sarc.prediction(sent['text'])
            d['hs'] = hs
            d['sarcasm'] = sarc
            # print(hs, sarc)
                                
            list_dicts.append(d)
            
        except Exception as e: print('<ERROR--->',sent['doc_id'], e)

    df = pd.DataFrame.from_records(list_dicts)

    return df
    
    
start = time.time()

inference_hs_sarc = hs_sarc.Predicting()

preprocess = preprocess.PreprocessingSpacy(params['language'][0])

sentiment_analysis = affective_analyses.Sentix()

emotion_analysis = affective_analyses.Emotions_NRC(params['language'][0])

texts = []
ids = []
dates = []

if params['data']['sentences'] != None:
    texts.extend(params['data']['sentences'])
    ids.extend([i for i in range(len(texts))])
    dates.extend([i for i in range(len(texts))])
else: 
    path = params['data']['input_file']
    df = preprocess_dataset.PrepareDF(params['data']['source'][0]).call_df(path)
    texts.extend(df['text'].tolist())
    ids.extend(df['id'].tolist())
    dates.extend(df['date'].tolist())

sents=[]
for idx, txt, date in zip(ids, texts, dates):
    sents.extend([{'date': date, 'doc_id': idx, 'text':txt, 'sent':' '.join(RegexpTokenizer(r'\w+').tokenize(x)), 'id':i} for i,x in enumerate(sent_tokenize(txt))])
print('length data: ', len(sents))

df_output = descriptive_analyses(sents)

finish = time.time()
# print(finish)

path = params['data']['output_file']
df_output.to_csv(path, sep=',', index=False)
# print(df_output)

print('taken time: ', finish-start)
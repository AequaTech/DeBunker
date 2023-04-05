import sys
sys.path.append('./aequa-tech_packages/') 
from analysis import affective_analyses
from dataset import preprocess_dataset
from text import preprocess

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
            d['doc_id'] = sent['doc_id']
            d['sent_id'] = sent['id']
            d['sent'] = sent['text']
            lemmatized_txt = preprocess.preprocess_sent(sent)['lemmatized']
            # print('-->', lemmatized_txt)
            if not d['sent']:
                continue
            
            # print('sentiment')
            d['positive'] = sentiment_analysis.sentiment_by_sent(lemmatized_txt)['positive']
            d['negative'] = sentiment_analysis.sentiment_by_sent(lemmatized_txt)['negative']
            
            # print('emotions')
            d_emo = emotion_analysis.emotions_by_sent(lemmatized_txt)
            for k, v in d_emo.items():
                    d[k] = v
                                
            list_dicts.append(d)
            
        except Exception as e: print('<ERROR--->', e)

    df = pd.DataFrame.from_records(list_dicts)

    return df
    
    
start = time.time()

preprocess = preprocess.PreprocessingSpacy(params['language'][0])

sentiment_analysis = affective_analyses.Sentix()

emotion_analysis = affective_analyses.Emotions_NRC(params['language'][0])

texts = []
ids = []

if params['data']['sentences'] != None:
    texts.extend(params['data']['sentences'])
    ids.extend([i for i in range(len(texts))])
else: 
    path = params['data']['input_file']
    df = preprocess_dataset.PrepareDF(params['data']['source'][0]).call_df(path)
    texts.extend(df['text'].tolist())
    ids.extend(df['id'].tolist())

sents=[]
for idx, txt in zip(ids, texts):
    sents.extend([{'doc_id': idx, 'text':' '.join(RegexpTokenizer(r'\w+').tokenize(x)), 'id':i} for i,x in enumerate(sent_tokenize(txt))])
print('length data: ', len(sents))

df_output = descriptive_analyses(sents)
finish = time.time()
# print(finish)

path = params['data']['output_file']
df_output.to_csv(path, sep=',', index=False)
# print(df_output)

print('taken time: ', finish-start)
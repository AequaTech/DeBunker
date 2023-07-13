import json

import requests
from datetime import datetime
import numpy as np

sentiment_analysis = affective_analyses.Sentix()

emotion_analysis = affective_analyses.Emotions_NRC('it')



#date=datetime.strptime('2023-04-28', '%Y-%M-%d')
#print(date)

page=requests.post('http://localhost:2000/api/v1/scrape',params={'url': 'https://www.pianetablunews.it/2023/04/28/si-rifiuta-di-andare-in-una-casa-di-riposo-senza-i-suoi-gatti-e-la-struttura-inaugura-un-piccolo-rifugio-per-accoglierli/' })


print(page.status_code)
print(type(page.text))
jsonResponse=json.loads(page.text)
print(json.dumps(jsonResponse))
request_id=json.loads(page.text)['result']['request_id']


page=requests.get('http://localhost:2000/api/v1/report_url/'+request_id)
print(page.text)


page=requests.get('http://localhost:2000/api/v1/danger/'+request_id)
print(page.text)
print(json.loads(page.text))

page=requests.get('http://localhost:2000/api/v1/sentiationalism/'+request_id)
print(page.text)
print(json.loads(page.text))
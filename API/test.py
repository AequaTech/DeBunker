import csv
import json
import time

import requests
from datetime import datetime
import numpy as np
import csv
#date=datetime.strptime('2023-04-28', '%Y-%M-%d')
#print(date)

#domain='130.192.212.85:9000'
domain='api.debunker-assistant.aequa-tech.com'
#domain='localhost:9001'


#text/html; charset=iso-8859-1

#url='http://saltoquantico.org//www.youtube.com/embed/qbW9cpsUBnU'
#resp = requests.request('HEAD', url,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
#print(resp)
#exit()
spamreader=csv.DictReader(open('test.csv'),delimiter=',',quotechar='"')
i=0
d={}
for row in spamreader:
    print(row['url'])
    #time.sleep(2)
    #if row['url'].split("/")[2] in d:
    #    continue

    page=requests.post('https://'+domain+'/api/v1/scrape',params={'url': row['url'] })

    print(page.status_code)
    print(page.text)
    #time.sleep(2)
    if page.status_code!=200:
        continue

    jsonResponse=json.loads(page.text)
    if jsonResponse['status']!=200:
        continue

    d[row['url'].split("/")[2]] = 0
    print(json.dumps(jsonResponse))
    request_id=json.loads(page.text)['result']['request_id']
    #time.sleep(1)
    #continue
    #page=requests.get('http://'+domain+'/api/v1/report_url/'+request_id)
    #print(page.text)


    page=requests.get('http://'+domain+'/api/v1/danger/'+request_id)
    print(page.text)
    print(json.loads(page.text))
    #continue
    page=requests.get('http://'+domain+'/api/v1/sentiationalism/'+request_id)
    print(page.text)
    print(json.loads(page.text))


    #page=requests.post('http://'+domain+'/api/v1/report_domain',params={'url': 'https://www.ilfattoquotidiano.it/in-edicola/articoli/2023/07/14/santanche-la-russa-laffare-villa-operazione-sospetta-i-pm-di-milano-e-la-finanza-indagano/7228717/' })
    #print(page.status_code)
    #print(page.text)
    #jsonResponse=json.loads(page.text)


    page=requests.get('http://'+domain+'/api/v1/echo_effect/'+request_id)
    print(page.text)
    print(json.loads(page.text))

    page=requests.get('http://'+domain+'/api/v1/reliability/'+request_id)
    print(page.text)
    print(json.loads(page.text))
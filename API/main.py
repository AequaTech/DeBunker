import json
import time
from random import randint
from fastapi import FastAPI

from webScraper.WebScraper import WebScraper
import hashlib

import sqlite3

app = FastAPI()

@app.get("/testing")
async def root():
    swap=[]
    lower = 1
    upper = randint(1000,10000)

    print("Prime numbers between", lower, "and", upper, "are:")
    numbers=''
    for num in range(lower, upper + 1):
        swap.append(num)
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                numbers+=' '+str(num)
    return {"message": "Prime numbers between"+str(lower)+"and"+str(upper)+"are: "+numbers}




@app.post("/api/v1/scrape")
async def retrieveUrl(url : str):
    hash_id = hashlib.md5(url.encode('utf-8')).hexdigest()
    con = sqlite3.connect("dubunkerAPI.db")
    cur = con.cursor()
    r=cur.execute("SELECT title, content, date from urls where hash_id=? limit 0,1",(hash_id,))
    row=r.fetchone()
    print(row)
    if row is None:
        webScraper=WebScraper()
        result=webScraper.scrape(url)
        jsonResult=json.loads(result)

        if jsonResult['status_code']==200:
            print(jsonResult)
            cur.execute("INSERT INTO urls (hash_id,title, content, date) VALUES (?,?,?,?)", (hash_id,jsonResult['title'],jsonResult['content'],jsonResult['date']))
            jsonResult['request_id'] = hash_id

        con.close()
        return json.dumps(jsonResult)

    else:

        con.close()
        return json.dumps({'request_id':row[0],'status_code':200,'title':row[1], 'content': row[2], 'date':row[3]})


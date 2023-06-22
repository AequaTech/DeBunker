import requests
import datetime
import numpy as np
page=requests.post('http://localhost:2000/api/v1/scrape',params={'url': 'https://www.pianetablunews.it/2023/04/28/si-rifiuta-di-andare-in-una-casa-di-riposo-senza-i-suoi-gatti-e-la-struttura-inaugura-un-piccolo-rifugio-per-accoglierli/' })


print(page.status_code)
print(page.text)

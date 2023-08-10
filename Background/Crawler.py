import logging
import time
from urllib.parse import urljoin
import requests
import tldextract
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls
        self.edges={}

    def download_url(self, url):
        time.sleep(2)
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):

        source_domain = tldextract.extract(url).domain

        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            logging.info(f'linked to: {url}')

            #self.add_url_to_visit(url)
            target_domain = tldextract.extract(url).domain
            if source_domain+' '+target_domain not in self.edges:
                self.edges[source_domain+' '+target_domain]=0
            self.edges[source_domain+' '+target_domain]+=1

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
        print(self.visited_urls)
        print(self.edges)

if __name__ == '__main__':
    Crawler(urls=['https://www.ilpost.it/']).run()
from datetime import datetime

import requests
from bs4 import BeautifulSoup


class ScrapePage:
    url_stem = 'https://efile.dcappeals.gov/public/caseView.do?csIID='

    def __init__(self, page_id, page_html, scraped_date):
        self.page_id = page_id
        self.page_html = page_html
        self.scraped_date = scraped_date

    @classmethod
    def from_request(cls, page_id):
        html = None
        response = requests.get(url=cls.url_stem + str(page_id))
        if response.ok:
            html = BeautifulSoup(response.content, 'html.parser')
        return cls(page_id=page_id, page_html=html, scraped_date=datetime.now())


if __name__ == '__main__':
    scrape = ScrapePage.from_request(58609)
    print(scrape)

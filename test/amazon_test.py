from bs4scraper import ParseType, SelectorField, Scraper, Selector
from bs4scraper.net import HtmlRequester

from pprint import pprint
from pydantic import BaseModel


class AmazonSelector(Selector):

    title: SelectorField = SelectorField(
        selector= ".s-title-instructions-style",
    )

    price: SelectorField = SelectorField(
        selector= ".a-price .a-offscreen"
    )

    img: SelectorField = SelectorField(
        selector= ".s-image", 
        data_from= ParseType.ATTRIBUTE,
        attribute= "src"
    )

    class Config:
        card_selector: str = ".puis-card-border"


class AmazonScraper(Scraper):

    def __init__(
        self, selector: AmazonSelector
    ):
        super().__init__(
            selector=selector,
            requester= HtmlRequester(
                headers= {
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                           'Accept-Language': 'en-US, en;q=0.5'
                },
                parse_type= "lxml"
            )
        )

    def get_url(
        self, product: str, page: int = 1
    ):
        return f"https://www.amazon.com/s?k={product}&page={page}"
    
    def scrape(
        self, product: str = "iphone"
    ):
        data = []

        for page in range(1, 4):
            data.extend(
                self.get_items(
                    url= self.get_url(product=product, page=page)
                )
            )

        return data 
    

selector = AmazonSelector()

amazon_items = AmazonScraper(selector=selector).scrape(
    product= "iphone"
)

pprint(amazon_items)

import pandas as pd


pd.DataFrame(amazon_items).to_csv("./data/amazon.csv")
from bs4scraper import (
    Scraper, Selector
)
from pydantic import create_model

from ..models import SimpleScraperModel
from ..utils import convert_selector_field

class APIScraper(Scraper):

    def __init__(self, selector):
        super().__init__(selector)

        self.url = None 

    def get_url(self):
        ... 

    def items(self, url: str):
        return self.get_items(url=url)


def simple_scraper_endpoint(
    request: SimpleScraperModel
)-> list[dict]:
    
    fields = convert_selector_field(request.css_selectors.fields)

    ScraperSelector = create_model(
        "ScraperSelector",
        __base__= Selector,
        **fields
    )

    ScraperSelector.Config = type("Config", (), {"card": request.css_selectors.card})

    scraper = APIScraper(selector= ScraperSelector())

    return scraper.items(
        url= request.website.url
    )
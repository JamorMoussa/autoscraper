from autoscraper import (
    Scraper, Selector
)
from pydantic import create_model

from ..models import BasicScraperModel
from ..utils import convert_selector_field

from fastapi import APIRouter

router = APIRouter(prefix="/scrape", tags=["items"])

class APIScraper(Scraper):

    def get_url(self):
        ... 

    def scrape(self, url: str):
        return self.get_items(url=url)


@router.post("/")
def basic_scraper_endpoint(
    request: BasicScraperModel
)-> list[dict]:
    
    fields = convert_selector_field(
        fields=request.css_selectors.fields
    )

    ScraperSelector = create_model(
        "ScraperSelector",
        __base__= Selector,
        **fields
    )

    ScraperSelector.Config = type(
        "Config", (), {
            "card_selector": request.css_selectors.card_selector
    })

    scraper = APIScraper(selector= ScraperSelector())

    return scraper.scrape(
        url= request.website.url
    )
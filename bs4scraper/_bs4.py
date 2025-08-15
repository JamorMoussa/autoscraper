from bs4scraper._base import (
    BaseScraper, SelectorField, BaseSelector, ParseType
)

__all__ = [
    "Scraper", "Selector", "ParseType", "SelectorField"
]

class Selector(BaseSelector):
    ... 

class Scraper(BaseScraper):
    ... 

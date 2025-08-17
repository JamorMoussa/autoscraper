from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Callable

from pydantic import BaseModel
from bs4 import BeautifulSoup, Tag

from .net import HtmlRequester


class ParseType(Enum):
    CONTENT = auto()
    ATTRIBUTE = auto()

class ToDict:

    def to_dict(self) -> dict:
        return self.model_dump()


class SelectorField(BaseModel, ToDict):

    selector: str 
    data_from: ParseType = ParseType.CONTENT
    attribute: str = ""
    processor: Callable = lambda x: x


class BaseSelector(BaseModel, ToDict):

    class Config:
        card_selector: str

    def __new__(cls, *args, **kwargs):

        assert hasattr(cls, "Config"), "Must define a 'Config' Class"
        assert hasattr(cls.Config, "card_selector"), "Must define a 'card_selector'"

        return super().__new__(cls, *args, **kwargs)
        

class BS4Parser:

    def __init__(
        self, selector: BaseSelector
    ):
        self.selector = selector

    def parse(
        self, bs4: BeautifulSoup
    ) -> list[dict]:
        
        data = []

        for card in bs4.select(self.selector.Config.card_selector):
            data.append(
                self.parse_data(card=card, selector=self.selector)
            )

        return data

    def parse_data(
        self, card: Tag, selector: BaseSelector
    ):
        data = {}

        for key, value in selector.to_dict().items():
            
            tag = card.select_one(value["selector"])

            out = None
            if tag:
                if value["data_from"] == ParseType.CONTENT:
                    out = tag.text
                elif value["data_from"] == ParseType.ATTRIBUTE:
                    out = tag[value["attribute"]]

            data[key] = value["processor"](out) if "processor" in value else out

        return data
    

class BaseScraper:
    
    def __init__(
        self,
        selector: BaseSelector, 
        requester = HtmlRequester() 
    ):
        self.selector = selector
        self.requester = requester
        self.parser = BS4Parser(selector= self.selector)

        self.url: str = None  
    
    def get_items(
        self, url: str 
    ):
        bs4 = self.requester.get(url=url)

        items = self.parser.parse(bs4=bs4)

        return items
    
    @abstractmethod
    def get_url(
        self, *args, **kwargs
    ) -> str:
        ... 

    @abstractmethod
    def scrape(self) -> list[dict]:
        ... 
    
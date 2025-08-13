from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Callable

from pydantic import BaseModel
from bs4 import BeautifulSoup
import requests


class ParseType(Enum):
    CONTENT = auto()
    ATTRIBUTE = auto()


class SelectorField(BaseModel):

    css_class: str 
    parse_type: ParseType = ParseType.CONTENT
    attr_name: str = ""
    processor: Callable = lambda x: x


class BaseSelector(BaseModel):

    class Config:
        card: str

    def to_dict(self) -> dict:
        return self.model_dump()
    

class BS4Parser:

    def __init__(
        self, selector: BaseSelector
    ):
        self.selector = selector

    def parse(
        self, bs4: BeautifulSoup
    ) -> list[dict]:

        parsed_items = []

        for item in bs4.find_all(class_ = self.selector.Config.card):
            
            item_dict = {}
            
            for field, selector_field in self.selector.to_dict().items():
                item_dict[field] =  (
                        self.parse_by(item, selector_field=selector_field)
                )
            
            parsed_items.append(item_dict)

        return parsed_items

    def parse_by(
        self, item, selector_field: SelectorField
    ):
        field = item.find(class_ = selector_field["css_class"])

        content = ""

        if selector_field["parse_type"] is ParseType.CONTENT:
            if field is not None:
                content = field.text
            else:
                content = ""
        elif selector_field["parse_type"] is ParseType.ATTRIBUTE:
            if field is None:
                field = item 
            content= field.get(selector_field["attr_name"])
            
        content = selector_field["processor"](content)

        return content
    

class Bs4Requester:

    def request(
        self, 
        url: str,
    ) -> BeautifulSoup:
        
        response = requests.get(url=url)

        bs4 = BeautifulSoup(
            markup=response.content, features='html.parser'
        )

        return bs4 
    

class BaseScraper:
    
    def __init__(
        self, selector: BaseSelector
    ):
        self.selector = selector
        self.bs4_requester = Bs4Requester()
        self.parser = BS4Parser(selector= self.selector)

        self.url: str = None  
    
    def get_items(
        self, url: str 
    ):
        bs4 = self.bs4_requester.request(url=url)

        items = self.parser.parse(bs4=bs4)

        return items
    
    @abstractmethod
    def get_url(
        self, *args, **kwargs
    ) -> str:
        ... 

    @abstractmethod
    def items(self) -> list[dict]:
        ... 
    
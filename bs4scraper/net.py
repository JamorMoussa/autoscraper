from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

class BaseHtmlRequester(ABC):

    def __init__(
        self, parse_type: str = 'html.parser'
    ):
        super().__init__()

        self.parse_type = parse_type

    @abstractmethod
    def get(
        self, url: str
    ) -> BeautifulSoup:
        ... 


class HtmlRequester(BaseHtmlRequester):

    def __init__(
        self, headers: dict = None, parse_type: str = 'html.parser'
    ):
        super().__init__(parse_type=parse_type)

        self.headers: dict = headers

    def get(
        self, url: str 
    ) -> BeautifulSoup:

        response = requests.get(
            url= url, headers=self.headers
        )

        bs4 = BeautifulSoup(
            markup=response.content, features= self.parse_type
        )

        return bs4 
from autoscraper.base import (
    BaseSelector, SelectorField
)

from pprint import pprint


class Selector(BaseSelector):

    title: SelectorField = SelectorField(
        selector= ".dev", 
    )

    img: SelectorField = SelectorField(
        selector= ".img"
    )


    class Config:
        card_selector: str = ".card"




selector = Selector()


pprint(selector.to_dict())
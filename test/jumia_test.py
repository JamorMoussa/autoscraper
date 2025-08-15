from bs4scraper import ParseType, SelectorField, Scraper, Selector

from pprint import pprint
from pydantic import BaseModel


class JumiaSelector(Selector):

    name: SelectorField = SelectorField(
        css_class= "name",
    )

    price: SelectorField = SelectorField(
        css_class= "prc",
        # processor= lambda prc: float(prc.split(" ")[0].replace(",", ""))
    )

    discount: SelectorField = SelectorField(
        css_class= "bdg _dsct _sm",
        processor= lambda pr: float(pr[:-1])/100 if pr != "" else 0
    )

    old_price: SelectorField = SelectorField(
        css_class = "old"
    )

    office: SelectorField = SelectorField(
        css_class = "bdg _mall _xs"
    )

    star: SelectorField = SelectorField(
        css_class = "stars _s",
        processor= lambda star: star.split(" ")[0]
    )

    img: SelectorField = SelectorField(
        css_class = "img",
        parse_type= ParseType.ATTRIBUTE,
        attr_name = "data-src"
    )

    img_width: SelectorField = SelectorField(
        css_class = "img",
        parse_type= ParseType.ATTRIBUTE,
        attr_name = "width", 
        processor= lambda width: width + "px"
    )

    class Config:
        card: str = "prd _fb col c-prd"


class JumiaScraper(Scraper):

    def __init__(self, selector):
        super().__init__(selector)

    def get_url(
        self, product: str, page: int
    ):
        return "".join([
            "https://www.jumia.ma/catalog/?q=",
            "+".join(product.split(" ")),
            f"?q={page}"
        ])
    
    def items(
        self, product: str
    ):
        all_items = []

        for i in range(1, 3):
            url = self.get_url(product=product, page=i)

            all_items.extend(self.get_items(url=url))

        return all_items 
    

selector = JumiaSelector()

jumia_items = JumiaScraper(selector=selector).items(
    product= "iphone"
)

pprint(jumia_items)

import pandas as pd


pd.DataFrame(jumia_items).to_csv("./data/jumia.csv")
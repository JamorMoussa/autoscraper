from bs4scraper.base import ParseType, SelectorField, BaseScraper, BaseSelector

from pprint import pprint


class JumiaSelector(BaseSelector):

    name: SelectorField = SelectorField(
        css_class= "name",
    )

    price: SelectorField = SelectorField(
        css_class= "prc",
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

    class Config:
        card: str = "prd _fb col c-prd"


class JumiaScraper(BaseScraper):

    def __init__(self, selector):
        super().__init__(selector)

    def get_url(
        self, product: str
    ):
        return "".join([
            "https://www.jumia.ma/catalog/?q=",
            "+".join(product.split(" "))
        ])
    
    def items(
        self, product: str
    ):
        url = self.get_url(product=product)

        return self.get_items(url=url)
    

selector = JumiaSelector()

jumia_items = JumiaScraper(selector=selector).items(
    product= "iphone"
)

pprint(jumia_items)
from pydantic import BaseModel

from typing import Literal, Optional, List, Dict


class FieldConfig(BaseModel):
    selector: str
    data_from: Literal["content", "attribute"] = "content"
    attribute: Optional[str] = ""
    processor: Optional[str] = "lambda x:x"


class CSSSelectors(BaseModel):
    fields: Dict[str, FieldConfig]
    card_selector: str


class WebsiteInfo(BaseModel):
    name: str
    url: str


class BasicScraperModel(BaseModel):
    website: WebsiteInfo
    css_selectors: CSSSelectors

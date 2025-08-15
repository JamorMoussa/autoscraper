from pydantic import BaseModel

from typing import Literal, Optional, List, Dict


class FieldConfig(BaseModel):
    css_class: str
    parse_type: Literal["content", "attribute"] = "content"
    attr_name: Optional[str] = ""
    processor: Optional[str] = "lambda x:x"


class CSSSelectors(BaseModel):
    fields: Dict[str, FieldConfig]
    card: str


class WebsiteInfo(BaseModel):
    name: str
    url: str


class SimpleScraperModel(BaseModel):
    website: WebsiteInfo
    css_selectors: CSSSelectors

from fastapi import APIRouter, Request

from .core.simple_scraper import simple_scraper_endpoint
from .models import SimpleScraperModel

router = APIRouter(
    prefix= "/api/v1/scrape",
    tags= ["api_v1", ]
)

@router.post("/")
def scrape(request: SimpleScraperModel):
    return simple_scraper_endpoint(request=request)
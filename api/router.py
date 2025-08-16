from fastapi import APIRouter

from .routes import (
    basic
)

router = APIRouter(
    prefix= "/api/v1",
    tags= ["api_v1"]
)

router.include_router(router=basic.router)


from fastapi import FastAPI
from core.sneakers_global import get_sneakers, get_description_all, get_sizes_all
from core.global_variables import URL
from core.nf_utils import get_number_of_pages_sneakers
import pandas as pd
from typing import Optional

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/get_sneaker_globals"}


@app.get("/api/v1/get_sneaker_globals")
def get_sneaker_globals(url: str = URL) -> Optional[str]:
    return get_sneakers(url).to_json()


@app.get("/api/v1/get_number_pages")
def get_number_of_pages(url: str = URL) -> int:
    return get_number_of_pages_sneakers(url)


@app.get("/api/v1/get_sneaker_description")
def get_snk_descr(url: str = URL) -> Optional[str]:
    return get_description_all(url).to_json()


@app.get("/api/v1/get_sneaker_sizes")
def get_snk_sizes(url: str = URL) -> Optional[str]:
    return get_sizes_all(url).to_json()

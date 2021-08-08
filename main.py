from fastapi import FastAPI
from core.sneakers_global import get_sneakers
from core.global_variables import URL
from core.nf_utils import get_number_of_pages_sneakers
import pandas as pd

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Visit the endpoint: /api/v1/get_sneaker_globals"}


@app.get("/api/v1/get_sneaker_globals")
def get_sneaker_globals(url: str = URL) -> pd.DataFrame:
    return get_sneakers(url)


@app.get("/api/v1/get_number_pages")
def get_number_of_pages(url: str = URL) -> int:
    return get_number_of_pages_sneakers(url)

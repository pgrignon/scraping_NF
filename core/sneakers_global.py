from bs4 import BeautifulSoup  # type: ignore
import pandas as pd
import requests

from core.sneakers_caracteristics import (
    get_sneaker_price,
    get_sneaker_name,
    get_sneaker_href,
)
from global_variables import URL


def get_sneakers(url: str = URL) -> pd.DataFrame:
    """
    Get the sneakers from the front page of the blog
    --------------
    Parameters:
        url: the URL to be scraped
    Returns:
        The dataframe with the global caracteristics of the sneakers
    """
    req = requests.get(URL)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    sneakers = soup.findAll(class_="grid-product__content")
    names = []
    prices = []
    href = []
    for sneaker in sneakers:
        names.append(get_sneaker_name(sneaker))
        prices.append(get_sneaker_price(sneaker))
        href.append(get_sneaker_href(sneaker))

    return pd.DataFrame({"Name": names, "Price": prices, "Ref": href})

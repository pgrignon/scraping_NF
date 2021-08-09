from bs4 import BeautifulSoup  # type: ignore
import pandas as pd
import requests

from core.sneakers_caracteristics import (
    get_sneaker_price,
    get_sneaker_name,
    get_sneaker_href,
)
from core.global_variables import URL
from core.sneakers_individual import get_description, get_sizes
from core.nf_utils import get_url_indiv_sneaker, get_pid_from_href


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
    pids = []
    for sneaker in sneakers:
        href_tmp = get_sneaker_href(sneaker)
        name_tmp = get_sneaker_name(sneaker)
        names.append(name_tmp)
        prices.append(get_sneaker_price(sneaker))
        href.append(href_tmp)
        pids.append(get_pid_from_href(href_tmp, name_tmp))

    return pd.DataFrame({"PID": pids, "Name": names, "Price": prices, "Ref": href})


def get_description_all(url: str = URL) -> pd.DataFrame:
    """
    Get the sneaker descriptions
    --------------
    Parameters:
        url: the URL to be scraped
    Returns:
        The df with the description column
    """
    req = requests.get(URL)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    sneakers = soup.findAll(class_="grid-product__content")
    pids = []
    description = []
    for sneaker in sneakers:
        href_tmp = get_sneaker_href(sneaker)
        name_tmp = get_sneaker_name(sneaker)
        pids.append(get_pid_from_href(href_tmp, name_tmp))
        href = get_sneaker_href(sneaker)
        description.append(get_description(get_url_indiv_sneaker(href)))

    return pd.DataFrame({"PID": pids, "Description": description})


def get_sizes_all(url: str = URL) -> pd.DataFrame:
    """
    Get the sneaker sizes
    --------------
    Parameters:
        url: the URL to be scraped
    Returns:
        The df with the booleans for each size
    """
    req = requests.get(URL)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    sneakers = soup.findAll(class_="grid-product__content")
    sizes = pd.DataFrame()
    for sneaker in sneakers:
        href_tmp = get_sneaker_href(sneaker)
        name_tmp = get_sneaker_name(sneaker)
        pid_tmp = get_pid_from_href(href_tmp, name_tmp)
        print(pid_tmp)
        print(href_tmp)
        sizes_tmp = get_sizes(get_url_indiv_sneaker(href_tmp), pid_tmp)
        sizes = pd.concat([sizes, sizes_tmp]).reset_index(drop=True)
        print(sizes)
    return sizes

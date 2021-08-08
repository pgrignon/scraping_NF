from bs4 import BeautifulSoup  # type: ignore
import requests
from typing import List, Dict


def concatenate_description(descr_list: List) -> str:
    """
    Concatenates the description of a sneaker
    --------------
    Parameters:
        descr_list: list of description items
    Returns:
        The description concatenated
    """
    return " | ".join(descr_list[1:])


def get_availability_size(size: str) -> bool:
    """
    Checks if a size is available or not
    --------------
    Parameters:
        size: the html code of a size
    Returns
        Boolean indicating if the considered size is available
    """
    return "disabled" not in size.get("class")  # type: ignore


def parse_size_value(size: str) -> int:
    """
    Parses the available size value
    --------------
    Parameters:
        size: the html code of a size
    Returns:
        The size downgraded if it is multi
    """
    return int(size.get("value").split("/")[0])  # type: ignore


def get_description(url: str) -> str:
    """
    Gets the description of a sneaker
    --------------
    Parameters:
        url: the url of the sneaker considered
    Returns:
        The description of the sneaker
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    sneaker = soup.find(class_="product-single__description rte").get_text()
    a = list(set(sneaker.split("\n")))
    a.remove("")
    return concatenate_description(a)


def get_sizes(url: str) -> Dict[int, bool]:
    """
    Gets the sizes available for a sneaker
    --------------
    Parameters:
        url: the url of the sneaker considered
    Returns:
        Dict containing the availability of all sizes
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    sizes = soup.find(class_="variant-input-wrap").find_all("input")
    sizes_dict = {}
    for size in sizes:
        sizes_dict[parse_size_value(size)] = get_availability_size(size)
    return sizes_dict

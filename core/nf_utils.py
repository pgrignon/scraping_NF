from bs4 import BeautifulSoup  # type: ignore
from core.global_variables import URL
import requests


def get_number_of_pages_sneakers(url: str = URL) -> int:
    """
    Get the number of pages for the sneaker category
    --------------
    Parameters:
        url: the url of the sneaker category
    Returns:
        The number of pages for the sneaker category
    """
    req = requests.get(URL)
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find(class_="pagination").get_text()
    return int(pages.replace("\n", "").split(" ")[-2])

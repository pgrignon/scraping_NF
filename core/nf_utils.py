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


def get_url_indiv_sneaker(href: str) -> str:
    return "https://noirfonce.eu" + href


def get_pid_from_href(href: str, name: str):
    """
    Get the PID of a sneaker
    --------------
    Parameters:
        href: the href of a sneaker
        name: the name of the sneaker
    Returns:
        The PID
    """
    pid_elts = href.split("/")[-1].split("-")[-2:]
    name_elts = name.lower().split(" ")
    for elt in pid_elts:
        if elt in name_elts:
            pid_elts.remove(elt)
    return "-".join(pid_elts)

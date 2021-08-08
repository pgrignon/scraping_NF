def get_sneaker_price(sneaker: str) -> float:
    """
    Get the price of a sneaker
    ---------------
    Parameters:
        sneaker: extract from source code zoomed on a sneaker
    Returns:
        The price of a sneaker
    """
    price: str = (
        sneaker.find(class_="grid-product__price")  # type: ignore
        .get_text()
        .replace("\n", "")
        .replace("€", "")
    )
    if len(price.split("Sale price")) > 1:
        return float(price.split("Sale price")[1])
    else:
        return float(price)


def get_sneaker_name(sneaker: str) -> str:
    """
    Get the name of a sneaker
    --------------
    Parameters:
        sneaker: extract from source code zoomed on a sneaker
    Returns:
        The name of a sneaker
    """
    return sneaker.find(
        class_="grid-product__title grid-product__title--body"
    ).get_text()  # type: ignore


def get_sneaker_href(sneaker: str) -> str:
    """
    Get the href link to the sneaker product
    --------------
    Parameters:
        sneaker: extract from source code zoomed on a sneaker
    Returns:
        The href link to the sneaker product
    """
    return sneaker.find("a").get("href")  # type: ignore

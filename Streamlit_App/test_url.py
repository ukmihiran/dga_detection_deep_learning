from urllib.parse import urlparse


def format_url(url):
    domain = url
    first_part = url[:4]
    if first_part == "http":
        domain = urlparse(url).netloc
    elif first_part == "www.":
        domain = url[4:]

    # if len(domain.split(".")[-1]) == 0:
    #     domain = f"{domain}.com"

    return domain


# print(format_url("asnmnkas"))


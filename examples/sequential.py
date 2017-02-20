from timeit import default_timer as timer

import requests

URLS = [
    "http://slowyourload.net/5/https://chrisheisel.com",
    "http://slowyourload.net/4/https://chrisheisel.com",
    "http://slowyourload.net/3/https://chrisheisel.com",
    "http://slowyourload.net/2/https://chrisheisel.com",
    "http://slowyourload.net/1/https://chrisheisel.com",
]


def get_url(url):
    print("GET {}".format(url))
    requests.get(url)
    print("\tDONE GET {}".format(url))


def main():
    print("Sequential ====================")
    start = timer()
    for url in URLS:
        get_url(url)
    end = timer()
    duration = (end - start)
    print("DONE in {} seconds".format(duration))


if __name__ == "__main__":
    main()

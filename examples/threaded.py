import threading

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
    print("Threaded ====================")
    start = timer()
    for url in URLS:
        t = threading.Thread(
            name="get_url - {}".format(url),
            target=get_url,
            args=(url, )
        )
        t.start()

    while len(threading.enumerate()) > 1:
        for t in threading.enumerate():
            if t is threading.main_thread():
                continue
            t.join()

    end = timer()
    duration = (end - start)
    print("DONE in {} seconds".format(duration))


if __name__ == "__main__":
    main()

"""
Thanks to http://skipperkongen.dk/2016/09/09/easy-parallel-http-requests-with-python-and-asyncio/ for the pattern.
"""

import asyncio

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


async def main(loop):
    print("Async ====================")
    start = timer()
    futures = []
    for url in URLS:
        future = loop.run_in_executor(None, get_url, url)
        futures.append(future)

    for response in await asyncio.gather(*futures):
        pass

    end = timer()
    duration = (end - start)
    print("DONE in {} seconds".format(duration))


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()

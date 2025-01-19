import requests


def get_request_worker(url: str):
    result = requests.get(url)
    print(result.headers)


def conveyor(num: int, url: str):
    for i in range(1, num):
        get_request_worker(url=url % str(i))


if __name__ == "__main__":
    conveyor(6, "https://jsonplaceholder.typicode.com/posts/%s")

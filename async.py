import response

import requests
from time import time

url = 'https://loremlickr.com/320/240'


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r

def write_file(responce):
    filename = responce.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)


def main():
    t0 = time()
    url = 'https://loremflickr.com/320/240'

    for i in range(10):
        write_file(get_file(url))

    print(time() - t0)

# if __name__ == '__main__':
#     main()


def write_img(data):
    filename = 'file{}.jpeg'.format(int(time()*100))
    with open(filename, 'wb') as file:
        file.write(data)

import asyncio
import aiohttp

async def fetch_cont(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_img(data)

async def main2():
    url = 'https://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_cont(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)

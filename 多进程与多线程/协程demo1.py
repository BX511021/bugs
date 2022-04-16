import asyncio
import re
import time

import aiohttp

# 获取链接
counter = 1


async def fn(url):
    global counter
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 Safari/537.36 "
    }
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url, headers=headers) as resp:
            # or_url = f"https://movie.douban.com/top250?start={num}&filter="

            # resp = requests.get(or_url, headers=headers)
            page_content = resp.text()
            obj1 = re.compile('<li>.*?<a href="(?P<url>.*?)">.*?width="100" alt="(?P<name>.*?)".*?</li>', re.S)
            page1 = obj1.finditer(await page_content)
            for i in page1:
                print("over!", i.group("name"), counter)
                counter = counter + 1


async def main():
    tasks = []
    for num in range(0, 250, 25):
        d = fn(f'https://movie.douban.com/top250?start={num}&filter=')
        tk = asyncio.create_task(d)
        tasks.append(tk)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    ori_loop=asyncio.new_event_loop()
    asyncio.set_event_loop(ori_loop)
    t1 = time.time()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
  #  asyncio.run(main())
    t2 = time.time()
    print("Great", t2 - t1)

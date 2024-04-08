import asyncio
import aiohttp
import os
from pathlib import Path
import aiofiles
import time
from functools import wraps


def async_measure_time(func):
    @wraps(func)
    async def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = await func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'Executed {func} in {elapsed:0.2f} seconds')
        return result

    return wrap


async def download_image(session, url, file_path):
    async with session.get(url) as response:
        if response.status == 200:
            file = await aiofiles.open(file_path, mode='wb')
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                await file.write(chunk)
            await file.close()

@async_measure_time
async def main(num_images, save_path):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(num_images):
            image_url = f'https://picsum.photos/1000/1000/?random={i}'
            filename = f'image_{i}.jpg'
            file_path = save_path / filename
            task = download_image(session, image_url, file_path)
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    num_images = 5 
    save_path = Path("img")
    save_path.mkdir(parents=True, exist_ok=True)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(num_images, save_path))
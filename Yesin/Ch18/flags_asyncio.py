import asyncio
import os
import sys
import time

import aiohttp

from Yesin.Ch17.flags import  BASE_URL, save_flags, show, main

# from ..Ch17.flags import BASE_URL, save_flags, show, main
POP20_CC = (
    'CN IN US ID BR PK NG BD RU JP '
    'MX PH VN ET EG ED IR TR CD KR').split()    # <2> 인구가 많은 순서대로 나열한 20개국에 마지막에 KR을 넣었음
BASE_URL = 'http://flupy.org/data/flags'    # <3> 국기 이미지를 갖고 있는 웹

DEST_DIR = '/Users/yesinkim/Bailando/Fluent-Python/Yesin/Ch17/flags/'


def save_flags(img, filename):
    """img(byte sequence)를 DEST_DIr안의 filename으로 저장"""
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)

def show(text):
    """문자열을 출력하고 `sys.stdout.flush()`를 호출해서 진행 상황을 한 줄에 출력한다.
    일반적으로 파이썬은 개행 문자를 받기 전까지 문자열을 출력하지 않으므로 `sys.stdout.flush()`를 호출해서 
    stdout 버퍼에 남아 있는 내용을 모두 화면에 출력하게 만들어야 한다."""
    print(text, end=' ')
    sys.stdout.flush()

def main(download_many):
    """download_many를 실행하는 데 걸린 시간을 기록하고 출력한다."""
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = f'\n{count} flags downloaded in {elapsed:.2f}s'
    print(msg)



@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image

@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


if __name__ == '__main__':
    main(download_many)
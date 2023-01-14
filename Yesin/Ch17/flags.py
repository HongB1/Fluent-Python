import os
import shutil
import sys
import time

import requests


POP20_CC = (
    'CN IN US ID BR PK NG BD RU JP '
    'MX PH VN ET EG ED IR TR CD KR').split()    # <2> 인구가 많은 순서대로 나열한 20개국에 마지막에 KR을 넣었음

BASE_URL = 'http://flupy.org/data/flags'    # <3> 국기 이미지를 갖고 있는 웹

DEST_DIR = '/Users/yesinkim/Bailando/Fluent-Python/Yesin/Ch17/flags/'

try:
    os.mkdir(DEST_DIR)
except:
    shutil.rmtree(DEST_DIR)
    os.mkdir(DEST_DIR)

def save_flags(img, filename):
    """img(byte sequence)를 DEST_DIr안의 filename으로 저장"""
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)

def get_flag(cc):
    """국가 코드를 인수로 받아서 URL을 만들고 이미지를 내려받는 함수
    응답으로 내려받은 이진 시퀀스를 반환
    """
    url = f"{BASE_URL}/{cc.lower()}/{cc.lower()}.gif"
    resp = requests.get(url)
    return resp.content

def show(text):
    """문자열을 출력하고 `sys.stdout.flush()`를 호출해서 진행 상황을 한 줄에 출력한다.
    일반적으로 파이썬은 개행 문자를 받기 전까지 문자열을 출력하지 않으므로 `sys.stdout.flush()`를 호출해서 
    stdout 버퍼에 남아 있는 내용을 모두 화면에 출력하게 만들어야 한다."""
    print(text, end=' ')
    sys.stdout.flush()

def download_many(cc_list):
    """동시성 버전과 다른 핵심부분이다 (무슨 말??)"""
    for cc in sorted(cc_list): # 국가 코드를 알파벳순으로 반복해서, 출력할 때 순서대로 나오도록 만든다. 내려받은 나라 수를 반환한다.
        image = get_flag(cc)
        show(cc)
        save_flags(image, cc.lower() + '.gif')
    return len(cc_list)

def main(download_many):
    """download_many를 실행하는 데 걸린 시간을 기록하고 출력한다."""
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = f'\n{count} flags downloaded in {elapsed:.2f}s'
    print(msg)


if __name__ == '__main__':
    main(download_many)
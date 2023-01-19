from concurrent import futures

from flags import save_flags, get_flag, show, main

MAX_WORKERS = 20

def download_one(cc):
    """하나의 이미지를 내려받는 함수.
    각 스레드에서 이 함수를 실행한다."""
    image = get_flag(cc)
    show(cc)
    save_flags(image, cc.lower() + '.gif')
    return cc

def download_many(cc_list):
    cc_list = cc_list[:5]   # 인구가 많은 다섯 나라만 사용
    with futures.ThreadPoolExecutor(max_workers=3) as executor:      # 대기중인 Future 객체를 출력해서 살펴보기 위해 workder를 3으로 하드코딩한다.
        to_do = []
        for cc in sorted(cc_list):  # 결과가 뒤바뀐다는 것을 확인하기 위해 국가 코드를 알파벳으로 정렬
            future = executor.submit(download_one, cc)  #executor.submit은 콜러블이 실행되도록 스케줄링하고 이 작업을 나타내는 Future 객체를 반환한다.
            to_do.append(future)    # 후에 as_completed()로 가져올 수 있도록 Future객체를 모두 저장한다.
            msg = f'Scheduled for{cc}: {future}'
            print(msg)  # 국가 코드와 해당 Future 객체를 출력

        results = []
        for future in futures.as_completed(to_do):  # Future가 완료될 때 해당 Future 객체를 생성한다.
            res = future.result()   # 이 Future 객체의 결과를 가져온다.
            msg = f'{future} result: {res}'
            print(msg)  # Future 객체와 이 객체의 결과를 출력한다.
            results.append(res)
    return len(results)


if __name__ == '__main__':
    main(download_many)


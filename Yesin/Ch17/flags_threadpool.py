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
    workers = min(MAX_WORKERS, len(cc_list))    # ThreadPoolExecutor에서 사용할 최대 스레드 수
    with futures.ThreadPoolExecutor(max_workers=workers) as executor:      # 모든 스레드가 완료되면 exit()메서드를 실행하고 executor.shutdown(wait=True) 메서드를 호출한다.
        res = executor.map(download_one, sorted(cc_list))       # 내장함수 map()과 비슷하게 작동한다. 함수가 반환한 값을 가져올 수 있도록 반복할 수 있는 제너레이터를 반환한다.

    # with futures.ProcessPoolExecutor() as executor:
    #     res = executor.map(download_one, sorted(cc_list)) 
    
    return len(list(res))   # 가져온 결과의 수를 반환한다. 스레드에서 호출한 함수 중 하나라도 예외를 발생시키면 , 암묵적으로 호출된 next()에서 반복자의 해당 반환값을 가져올 때와 마찬가지로 여기에서 예외가 발생한다.

if __name__ == '__main__':
    main(download_many)
# [18-2]spinner_asyncio.py: 스레드로 텍스트 스피너 애니메이트 하기
import asyncio
import itertools
import sys

@asyncio.coroutine
def spin(msg): 
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):   # <3> itertools.cycle()은 주어진 시퀀스를 순환하면서 끝없이 항목을 생성하므로, 이 for 루프는 사실상 무한 루프임
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))     # <6> 공백 문자로 덮어쓰고 다시 커서를 처음으로 이동해서 메시지 출력 행을 청소한다.

@asyncio.coroutine
def slow_function():    # <7> 실행에 시간이 오래걸리는 함수라고 친다.
    # 입출력을 위해 장시간 기다리는 것처럼 보이게 만든다.
    yield from asyncio.sleep(3)   # <8>  주 스레드에서 sleep() 함수를 호출할 때 GIL이 해제되므로 두 번째 스레드가 진행된다.
    return 42

@asyncio.coroutine
def supervisor():   # <9> 이 함수는 두 번째 스레드를 만들고, 스레드 객체를 출력하고, 시간이 오래 걸리는 연산을 수행하고 나서 스레드를 제거한다.
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner obj:', spinner)  # <10> 두번 째 스레드 객체를 출력한다.
    result = yield from slow_function()    # <12> 함수 실행함. 그러면 주 스레드가 블로킹되고, 그 동안 두 번째 스레드가 스피너 애니메이션을 보여준다.
    spinner.cancel()
    return result

def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)

if __name__ == '__main__':
    main()

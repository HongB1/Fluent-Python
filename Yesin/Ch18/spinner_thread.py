# [18-1]spinner_thread.py: 스레드로 텍스트 스피너 애니메이트 하기
import threading
import itertools
import time
import sys

class Signal:   # <1> 외부에서 스레드를 제어하기 위한 간단한 가변 객체임
    go = True

def spin(msg, signal):  # <2> 이 함수는 별도의 스레드에서 실행된다. signal은 <1>의 객체를 받음.
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):   # <3> itertools.cycle()은 주어진 시퀀스를 순환하면서 끝없이 항목을 생성하므로, 이 for 루프는 사실상 무한 루프임
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:   # <5> go 속성이 False면 루프를 타출함.
            break
    write(' ' * len(status) + '\x08' * len(status))     # <6> 공백 문자로 덮어쓰고 다시 커서를 처음으로 이동해서 메시지 출력 행을 청소한다.

def slow_function():    # <7> 실행에 시간이 오래걸리는 함수라고 친다.
    # 입출력을 위해 장시간 기다리는 것처럼 보이게 만든다.
    time.sleep(3)   # <8>  주 스레드에서 sleep() 함수를 호출할 때 GIL이 해제되므로 두 번째 스레드가 진행된다.
    return 42

def supervisor():   # <9> 이 함수는 두 번째 스레드를 만들고, 스레드 객체를 출력하고, 시간이 오래 걸리는 연산을 수행하고 나서 스레드를 제거한다.
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner obj:', spinner)  # <10> 두번 째 스레드 객체를 출력한다.
    spinner.start()     # <11> 두번째 스레드 실행
    result = slow_function()    # <12> 함수 실행함. 그러면 주 스레드가 블로킹되고, 그 동안 두 번째 스레드가 스피너 애니메이션을 보여준다.
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print('Answer:', result)


if __name__ == '__main__':
    main()
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write   # <2> 원래의 sys.stdout.write를 보관한다.

    def reverse_write(text):    # <3> reverse 함수 정의. origianl_write는 클로저를 통해 접근할 수 있다.
        original_write(text[::-1])

    sys.stdout.write = reverse_write    # <4> sys.stdout.write()를 reverse_write로 교체한다.
    yield 'JABBERWOCKY'     # <5> with 문의 as 절에 있는 타겟 변수에 바인딩 될 값을 생성한다. with문의 본체가 실행되는 동안 이 함수는 여기에서 실행을 일시 중단한다.
    sys.stdout = original_write     # <6> 제어흐름이 with 블록을 빠져나오면 yield 문 이후의 코드가 실행된다. 여기서는 원래의 sys.stdout.write() 메서드를 복원한다.
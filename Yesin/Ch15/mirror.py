class LookingGlass:

    def __enter__(self):    # <1> self 인수만 들어감
        import sys
        self.original_write = sys.stdout.write      # <2> 후에 사용하기 위해 저장함.
        sys.stdout.write = self.reverse_write       # <3> 멍키패칭으로 직접 만든 메서드로 변경
        return 'JABBERWOCKY'        # <4> 타깃 변수 what에 무언가를 저장하기 위해 문자열 반환

    def reverse_write(self, text):      # <5> sys.std.wrte()은 몽키패칭되었기 때문에 text를 거꾸로 뒤집고 원래의 sys.stdout.write()함수를 호출한다.
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):     # <6> 정상적으로 수행이 완료되면 파이썬은 None, None, None 인수로 __exit__() 메서드를 호출한다. 예외가 발생한 경우에는 이 세 개의 인수에 예외 데이터가 전달된다.
        import sys      # <7> 파이썬은 임포트된 모듈을 캐시에 저장하므로 그 다음에 모듈을 임포트 하면 간단히 처리된다(뭐가 처리된다는 말?)
        sys.stdout.write = self.original_write      # <8> sys.stdout.write()를 원해 메서드로 변경한다.
        if exc_value is ZeroDivisionError:      # <9> exception 인수가 ZeroDivisionError면 메시지를 출력한다.
            print('Please DO NOT divide by zero')
            return True     # <10> True를 반환해 예외가 처리되었음을 파이썬 인터프리터에 알려준다.
            # <11> __exit__()가 None이나 True 이외의 값을 반환하면 with 블록에서 발생한 예외가 상위 코드로 전달된다.
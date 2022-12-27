# 예제 15-3 mirror.py: LookingGlass 콘텍스트 관리자 클래스 코드
class LookingGlass:
    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write  # sys.stdout.write()를 멍키 패칭
        return 'JABBERWOCKY'  # 타깃 변수 what에 저장

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  
        # 정상적으로 수행되면 None, None, None 인수로 전달되며,
        # 예외가 발생한 경우에는 이 세 개의 인수에 예외 데이터가 전달됌
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True  # 예외가 처리되었음을 True를 통해 파이썬 인터프리터에게 알림. 
        # None이나 True 이외의 값이 반환되면 with 블록에서 발생한 예외가 상위 코드로 전달됌

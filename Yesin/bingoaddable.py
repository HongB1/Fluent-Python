import itertools    # <1>. 펴준 라이브러리 임포트 first

from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):      # <2> 상속티비

    def __add__(self, other):
        if isinstance(other, Tombola):  # <3> add 메서드는 other가 Tombola 객체일 때만 작동한다.
            return AddableBingoCage(self.inspect() + other.inspect())    # <4> other 객체에서 항목을 가져온다.
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:    # <5> Tombola가 아닐 때는 other의 반복자를 가져온다.
                other_iterable = iter(other)
            except TypeError:   # <6> 실패하면 메세지와 함께 예외를 발생시킨다. 가능하면 에러 메시지에 사용자가 문제를 해결할 방밥을 명확히 알려주는 것이 좋다.
                self_cls = type(self).__name__
                msg = 'right operand in += must be {!r} or and iterable'
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)   # <7> 이제 로드해줄 수 있다.
        return self     # <8> 가장 중요하다. 할당 연산 특별 메서드는 반드시 self를 반환해야 한다.
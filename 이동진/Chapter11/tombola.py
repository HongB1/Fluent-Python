# 예제 11-9 tombola.py: 추상 메서드 두 개와 구상 메서드 두개를 가진 Tombola ABC
import abc


class Tombola(abc.ABC):  # ABC를 정의하려면 abc.ABC를 상속해야 한다.

    @abc.abstractmethod  # 추상 메서드임을 데커레이터로 표시한다. docstring만 넣는 경우가 종종 있다.
    def load(self, iterable):
        """iterable의 항목들을 추가한다."""

    @abc.abstractmethod
    def pick(self):  # docstring을 통해 LookupError를 발생시키라고 알려준다.
        """무작위로 항목을 하나 제거하고 반환한다.
        객체가 비어 있을 때 이 메서드를 실행하면 `LookupError`가 발생한다.
        """

    def loaded(self):  # ABC에도 구상 메서드가 들어갈 수 있다. 구상 메서드들은 반드시 ABC에 정의된 인터페이스만 사용해야 한다.
        """최소 한 개의 항목이 있으면 True를, 아니면 False를 반환한다."""
        return bool(self.inspect())

    def inspect(self):
        """현재 안에 있는 항목들로 구성된 정렬된 튜플을 반환한다."""
        items = []
        while True:  # 서브 클래스가 어떻게 항목을 저장하는지 모르기 때문에 이렇게 정의한다.
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

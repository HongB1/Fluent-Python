import math
import numbers
import reprlib
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)  # '보호된' 객체 속성

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        class_name = type(self).__name__
        components = reprlib.repr(self._components)  # 제한된 길이로 표현
        components = components[components.find('['):-1]  # "arra('d'"와 마지막 괄호 제거
        return f'{class_name}({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(self._components))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = f'{cls.__name} indices must be integers'
            raise TypeError(msg)

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        raise AttributeError(f'{cls.__name__!r} object has no attribute {name!r}')

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shortcut_names:
                error = 'read-only attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)  # 에러가 발생하지 않으면 표준 동작을 위해 슈퍼클래스의 __setattr__() 메서드를 호출

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

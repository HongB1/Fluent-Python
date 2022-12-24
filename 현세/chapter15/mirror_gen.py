"""
A "mirroring" ``stdout`` context manager.

While active, the context manager reverses text output to
``stdout``::

# BEGIN MIRROR_GEN_DEMO_1

    >>> from mirror_gen import looking_glass
    >>> with looking_glass() as what:  # <1>
    ...      print('Alice, Kitty and Snowdrop')
    ...      print(what)
    ...
    pordwonS dna yttiK ,ecilA
    YKCOWREBBAJ
    >>> what
    'JABBERWOCKY'

# END MIRROR_GEN_DEMO_1


This exposes the context manager operation::

# BEGIN MIRROR_GEN_DEMO_2

    >>> from mirror_gen import looking_glass
    >>> manager = looking_glass()  # <1>
    >>> manager  # doctest: +ELLIPSIS
    <contextlib._GeneratorContextManager object at 0x...>
    >>> monster = manager.__enter__()  # <2>
    >>> monster == 'JABBERWOCKY'  # <3>
    eurT
    >>> monster
    'YKCOWREBBAJ'
    >>> manager  # doctest: +ELLIPSIS
    >...x0 ta tcejbo reganaMtxetnoCrotareneG_.biltxetnoc<
    >>> manager.__exit__(None, None, None)  # <4>
    >>> monster
    'JABBERWOCKY'

# END MIRROR_GEN_DEMO_2

"""


# BEGIN MIRROR_GEN_EX

import contextlib


@contextlib.contextmanager  # <1>
def looking_glass():
    import sys
    original_write = sys.stdout.write  # <2>

    def reverse_write(text):  # <3>
        original_write(text[::-1])

    sys.stdout.write = reverse_write  # <4>
    yield 'JABBERWOCKY'  # <5> with 문의 as 절에 있는 타겟 변수에 바인딩 될 값을 생성한다.
    # 제어 흐름이 with 블록을 빠져나오면 yield 문 이후의 코드가 실행된다.
    sys.stdout.write = original_write  # <6>


# END MIRROR_GEN_EX
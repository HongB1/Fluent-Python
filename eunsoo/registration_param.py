#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 함수의 추가와 제거를 빠르게 하기 위해 registry를 집합형으로 정의한다. 
registry = set()  

# register()는 선택적 키워드 인수를 받는다. 
def register(active=True):  
    # decorate() 내부 함수가 실제 데커레이터다.
    def decorate(func):  
        print('running register'
              f'(active={active})->decorate({func})')
        if active:   # 클로저에서 읽어온 active 인수가 True일 때만 func를 등록한다. 
            registry.add(func)
        else:
            registry.discard(func)  # active가 True가 아니고 func가 registry에 들어있으면 제거한다. 

        return func  # decorate()는 데커레이터이므로 함수를 반환한다. 
    return decorate  # register()는 데커레이터 팩토리이므로 decorate()를 반환한다. 

@register(active=False)  # @register 팩토리는 원하는 매개변수와 함께 함수로 호출해야 한다. 
def f1():
    print('running f1()')

@register()  # 인수를 전달하지 않더라도 register는 여전히 함수로 호출해야 하므로 @register() 형태로 호출한다. 
def f2():
    print('running f2()')

def f3():
    print('running f3()')


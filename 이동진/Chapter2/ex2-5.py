'''
제너레이터 표현식에서 튜플과 배열 초기화하기
'''
import array

symbols = 'I love you'
codes = tuple((ord(symbol) for symbol in symbols))
print(codes)

# array.array의 첫 번째 인자는 typecode이며 어떤 자료형을 입력 받는지 나타냄
codes = array.array('I', (ord(symbol) for symbol in symbols))
print(codes)

'''
지능형 리스트와 맵/필터 구성으로 만든 동일 리스트
'''
symbols = 'I love you'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 100]
print(beyond_ascii)

beyond_ascii = list(filter(lambda c:c > 100, map(ord, symbols)))
print(beyond_ascii)

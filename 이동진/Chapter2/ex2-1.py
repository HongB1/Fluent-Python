'''
문자열에서 유니코드 코드포인트 리스트 만들기 (버전1)
'''
symbols = 'I love you'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))  # ord returns the Unicode code point of a character
    
print(codes)

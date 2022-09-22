'''
문자열에서 유니코드 코드포인트 리스트 만들기 (버전2)
'''
symbols = 'I love you'
codes  = [ord(symbol) for symbol in symbols]
print(codes)

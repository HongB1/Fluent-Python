#%%
from collections import namedtuple

Member = namedtuple('Member', ['name', 'age', 'height', 'weight'])

teams = [
    Member('이동진', 29, 179, 70),
    Member('홍길동', 24, 173, 65),
    Member('서장훈', 49, 205, 115),
    Member('이하늘', 31, 165, 53),
    Member('강호동', 53, 183, 110),
]

name, age, height, weight = zip(*teams)

print(name)
print(age)
print(height)
print(weight)
print()
#%%
print("======================")
A = ('A', 'B', 'C')
B = (1, 2, 3)
for i in zip(A, B):
    print(i)
print("")

print("======================")
#%%
x = [
    (1, 2, 3, 4, 5),
    (6, 7, 8, 9, 10),
    (11, 12, 13, 14, 15)
]
print(*x)
for i in zip((1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14 ,15)):
    print(i)

# %%

print("가나다 abc 123")
print("가나다", "abc 123")
print("가나다", "abc", "123")

def func(*args):
    print(args)
    print(type(args))

func(1,2)

def sumall(**nums):
    print(nums)
    result = 0
    for num in nums:
        result += num
    return result

sumall(a=1,b=2,c=3)

def sum(a,b,c):
    return a+b-c

sum(*(1,2,3))
sum(**{'a':4, 'b':7, 'c':10})

from tqdm import tqdm
import time
aaa ="String"
# 진행 상황 표시
for _ in tqdm(aaa):
    time.sleep(1) # 각 반복마다 1초 대기

for ii in tqdm(range(50), desc="tqdm example", mininterval=10):
    time.sleep(1)
import math

n = 100
array = [True for i in range(n+1)]

for i in range(2,int(math.sqrt(n) + 1)): # n보다 작은 수 m = ab라면, a,b 중 적어도 하나는 sqrt(n)이하 
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1
      
for i in range(2,n + 1):
  if array[i]:
    print(i,end=' ')
    
# 시간 복잡도 O(NloglogN) -> 빠르지만 많은 메모리 차지할수도..

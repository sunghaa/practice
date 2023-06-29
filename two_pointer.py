a = [1,5,9]
b = [2,4,6,8]
n,m = 3,4

result = [0] * (n+m)
i=0
j=0
k=0

while i < n or j < m:
  if j>=m or (i<n and a[i]<= b[j]): #b리스트 모두 끝 or a의 원소가 더 작을 때
    result[k] = a[i]
    i += 1
  else: # a리스트 모두 끝 or b의 원소가 더 작을때
    result[k] = b[j]
    j += 1
  k += 1
  
for i in result:
  print(i,end=' ')
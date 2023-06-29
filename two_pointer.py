n = 5 # 데이터 개수
m = 5 # 목표 부분합
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1
  if interval_sum == m: # 부분합 >= m 이면 start+1 하며 다음 경우로 넘어감
    count += 1
  interval_sum -= data[start]
  
print(count)
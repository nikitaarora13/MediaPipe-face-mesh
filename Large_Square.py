import math
for i in range(int(input())):
    n, m = map(int, input().split())
    p = m*(int(math.sqrt(n)))
    print(p)

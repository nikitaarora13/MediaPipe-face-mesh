T = int(input())
for i in range(T):
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    l = arr[2]

    a = []
    for i in range(m):
        b = list(map(int, input().split()))
        a.append(b[1:])

    strip = list(map(int, input().split()))
    length = 1

    id = {}
    for i, g in enumerate(a):
        for e in g:
            id.setdefault(e, set()).add(i)

    def group(e1, e2):
        return id.get(e1, set()) & id.get(e2, set())

    for i in range(len(strip)-1):
        if(group(strip[i], strip[i + 1]) == set()):
            length += 1

    print(length)

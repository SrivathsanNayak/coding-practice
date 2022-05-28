t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split())) #space-separated input
    a.reverse()
    print(*a) #space-separated output

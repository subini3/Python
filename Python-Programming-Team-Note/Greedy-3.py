
n = int(input())
data = list(map(int, input().split()))
data.sort()

grup = 0
members = 0

for i in data:
    members += 1
    if members >= i:
        grup += 1
        members = 0
print(grup)



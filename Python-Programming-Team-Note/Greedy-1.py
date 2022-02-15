
N = map(int, input().split())
count = 0
while True:
    target = (N//K) * K  # 가장 가까운 K로 나누어 지는 수를 target으로
    count += (N - target)  # N에서 target을 빼게 되면 -1 을 몇번 해야 하는지 구할 수 있다.
    N = target  # 빼고 나면 N은 target이 된다(K로 나누어 진다.)
    if N < K:  # N이 K보다 작을 때 반복문 종료
        break
    N //= K
    count += 1

print(count - 1)

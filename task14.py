n = int(input())
t = 9 * 60 + 45 * n + 5 * (n // 2) + 15 * ((n - 1) // 2)
print(t // 60, t % 60)